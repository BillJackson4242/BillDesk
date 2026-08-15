#!/usr/bin/env python3
"""
batch_synthesize.py — Claudian Wiki batch synthesis via Anthropic Message Batches API

Drop-in enhancement for auto_synthesize.py. Submits all pending seed pages as a
single batch rather than processing sequentially. At Haiku 4.5 batch pricing
($0.50/$2.50 per MTok), 512 pages runs under $2 total vs. 100+ nights of Ollama.

FERPA NOTE: Do NOT run student submission content through this script. Use Ollama
(auto_synthesize.py) for any content derived from student work. Batch results are
stored on Anthropic servers for 29 days and are not eligible for Zero Data Retention.

Usage:
    python batch_synthesize.py --vault-path "C:/path/to/OBSIDIAN_VAULT" [--limit 50] [--domain teaching]
    python batch_synthesize.py --vault-path "C:/path/to/OBSIDIAN_VAULT" --status <batch_id>
    python batch_synthesize.py --vault-path "C:/path/to/OBSIDIAN_VAULT" --collect <batch_id> [--wait]
"""

import os
import json
import time
import hashlib
import argparse
from pathlib import Path
from datetime import datetime

import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

MODEL = "claude-haiku-4-5"  # Batch pricing: $0.50/$2.50 per MTok
MAX_TOKENS = 1500
BATCH_STATE_FILE = ".batch_state.json"

SYNTHESIS_SYSTEM = """You are synthesizing a wiki page for the Claudian Knowledge Vault, a personal knowledge base for Bill Jackson (adjunct faculty, business communication specialist, OCM consultant).

Convert seed content into a complete, well-structured wiki page. Keep it:
- Specific and factual (no vague generalities)
- Under 600 words unless the content demands more
- Written in plain prose with headers where genuinely useful
- Free of corporate filler and AI-register language

Write for a reader who already knows the domain. No preamble, no meta-commentary about what you are doing."""


def load_batch_state(vault_path: Path) -> dict:
    state_file = vault_path / BATCH_STATE_FILE
    if state_file.exists():
        return json.loads(state_file.read_text())
    return {}


def save_batch_state(vault_path: Path, state: dict):
    state_file = vault_path / BATCH_STATE_FILE
    state_file.write_text(json.dumps(state, indent=2))


def path_to_custom_id(rel_path: str) -> str:
    """Deterministic custom_id from relative path. Must match ^[a-zA-Z0-9_-]{1,64}$"""
    return hashlib.md5(rel_path.encode()).hexdigest()


def find_pending_seeds(vault_path: Path, domain: str = None, limit: int = None) -> list:
    raw_dir = vault_path / "raw" / "converted"
    wiki_dir = vault_path / "wiki"

    if not raw_dir.exists():
        raise FileNotFoundError(f"Seeds directory not found: {raw_dir}")

    pattern = f"**/{domain}/**/*.md" if domain else "**/*.md"
    pending = []

    for seed_path in sorted(raw_dir.glob(pattern)):
        rel = seed_path.relative_to(raw_dir)
        wiki_path = wiki_dir / rel
        if not wiki_path.exists():
            pending.append(seed_path)

    if limit:
        pending = pending[:limit]
    return pending


def submit_batch(vault_path: Path, seeds: list) -> str:
    client = anthropic.Anthropic()
    raw_dir = vault_path / "raw" / "converted"

    requests = []
    id_to_path = {}

    for seed_path in seeds:
        seed_content = seed_path.read_text(encoding="utf-8", errors="replace")
        rel = str(seed_path.relative_to(raw_dir))
        custom_id = path_to_custom_id(rel)
        id_to_path[custom_id] = str(seed_path)

        requests.append(
            Request(
                custom_id=custom_id,
                params=MessageCreateParamsNonStreaming(
                    model=MODEL,
                    max_tokens=MAX_TOKENS,
                    system=[
                        {
                            "type": "text",
                            "text": SYNTHESIS_SYSTEM,
                            "cache_control": {"type": "ephemeral"},
                        }
                    ],
                    messages=[
                        {
                            "role": "user",
                            "content": f"Seed content:\n\n{seed_content[:8000]}\n\nWrite the wiki page now.",
                        }
                    ],
                ),
            )
        )

    batch = client.messages.batches.create(requests=requests)

    state = load_batch_state(vault_path)
    state[batch.id] = {
        "submitted_at": datetime.utcnow().isoformat(),
        "id_to_path": id_to_path,
    }
    save_batch_state(vault_path, state)

    print(f"Batch submitted: {batch.id}")
    print(f"Requests: {len(requests)}")
    print(f"Status: {batch.processing_status}")
    print(f"\nCheck status:  python batch_synthesize.py --vault-path {vault_path} --status {batch.id}")
    print(f"Collect:       python batch_synthesize.py --vault-path {vault_path} --collect {batch.id} [--wait]")
    return batch.id


def check_status(batch_id: str) -> str:
    client = anthropic.Anthropic()
    batch = client.messages.batches.retrieve(batch_id)
    counts = batch.request_counts
    print(f"Batch: {batch_id}")
    print(f"Status: {batch.processing_status}")
    print(f"  Processing: {counts.processing}")
    print(f"  Succeeded:  {counts.succeeded}")
    print(f"  Errored:    {counts.errored}")
    print(f"  Expired:    {counts.expired}")
    print(f"  Canceled:   {counts.canceled}")
    return batch.processing_status


def collect_results(vault_path: Path, batch_id: str):
    client = anthropic.Anthropic()
    state = load_batch_state(vault_path)

    if batch_id not in state:
        raise ValueError(f"No local record for batch {batch_id}. Was it submitted from this vault?")

    id_to_path = state[batch_id]["id_to_path"]
    raw_dir = vault_path / "raw" / "converted"
    wiki_dir = vault_path / "wiki"

    written = errored = 0

    for result in client.messages.batches.results(batch_id):
        path_str = id_to_path.get(result.custom_id)
        if not path_str:
            print(f"  WARNING: no path for custom_id {result.custom_id}")
            continue

        seed_path = Path(path_str)
        rel = seed_path.relative_to(raw_dir)
        wiki_path = wiki_dir / rel

        match result.result.type:
            case "succeeded":
                wiki_path.parent.mkdir(parents=True, exist_ok=True)
                text = result.result.message.content[0].text
                wiki_path.write_text(text, encoding="utf-8")
                written += 1
            case "errored":
                print(f"  FAILED ({result.result.error.type}): {rel}")
                errored += 1
            case "expired":
                print(f"  EXPIRED: {rel}")
                errored += 1
            case "canceled":
                print(f"  CANCELED: {rel}")
                errored += 1

    print(f"\nDone. Written: {written} | Errors/Expired/Canceled: {errored}")

    del state[batch_id]
    save_batch_state(vault_path, state)


def main():
    parser = argparse.ArgumentParser(
        description="Claudian Wiki batch synthesis via Anthropic Batches API",
        epilog="FERPA NOTE: Never run student submission content through this script.",
    )
    parser.add_argument("--vault-path", required=True, help="Path to OBSIDIAN_VAULT root")
    parser.add_argument("--limit", type=int, default=None, help="Max seeds to submit")
    parser.add_argument("--domain", default=None, help="Filter by domain (e.g. teaching, tools)")
    parser.add_argument("--status", metavar="BATCH_ID", help="Check status of a submitted batch")
    parser.add_argument("--collect", metavar="BATCH_ID", help="Collect results for a completed batch")
    parser.add_argument("--wait", action="store_true", help="With --collect: poll until done, then collect")
    args = parser.parse_args()

    vault_path = Path(args.vault_path)

    if args.status:
        check_status(args.status)
        return

    if args.collect:
        if args.wait:
            print(f"Polling {args.collect}...")
            while True:
                status = check_status(args.collect)
                if status == "ended":
                    break
                print("  Waiting 60s...")
                time.sleep(60)
        collect_results(vault_path, args.collect)
        return

    print("Finding pending seeds...")
    seeds = find_pending_seeds(vault_path, domain=args.domain, limit=args.limit)

    if not seeds:
        print("No pending seeds found.")
        return

    print(f"Found {len(seeds)} pending seeds.")
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set.")
        return

    submit_batch(vault_path, seeds)


if __name__ == "__main__":
    main()

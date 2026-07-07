---
title: Build Index Reference
domain: vessels
created: 2026-05-18
updated: 2026-07-06
sources: 
status: draft
tags: 
synthesized: 2026-05-19
synthesized_by: ollama/qwen2.5:7b
---

# Build Index Reference

## Summary
The `build_index.py` script is a foundational tool in the Memory Bridge Kit that scans directories to create an index of specific file types. This index supports further processing and analysis within the project.

## Key Points
- **Purpose:** Scans recursively for `.txt`, `.md`, `.py`, and `.json` files, generating a `memory_index.json` file.
- **Usage:** Executed via `python bridgekit/core/scripts/build_index.py /path/to/target/folder`.
- **Output:** A JSON file containing indexed files categorized by their extensions.
- **Dependencies:** Requires Python 3.8 or higher.
- **Project Context:** Part of the Memory Engine 2.0 project, contributing to file parsing and vault mapping processes.

## Notes
None.

---

## Connections

- [[authors]]
- [[index]]
- [[memory-engine]]

## Sources

- [Build Index Reference.md](OBSIDIAN_VAULT/notes/insights/Build Index Reference.md)

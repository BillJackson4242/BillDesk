---
title: Appendix E Conversionrecovery
domain: vessels
created: 2026-05-18
updated: 2026-07-23
sources: 
status: draft
tags: 
synthesized: 2026-05-19
synthesized_by: ollama/qwen2.5:7b
---

# Appendix E Conversionrecovery

## Summary
This document provides tips on converting Markdown to Word and manual recovery procedures for an AI assistant named "Conversion & Recovery Tips."

## Key Points
- **Converting Markdown to Word:**
  - Use Pandoc with the command `pandoc filename.md -o filename.docx`.
  - Utilize online converters like dillinger.io or markdowntodocx.com.
  - Copy and paste content from Obsidian into a new Word document.

- **Reseed Recovery Sequence:**
  - **Phase 1: Cold Start** involves pasting `Vault_Reseed_Startup.md` and waiting for confirmation.
  - **Phase 2: Manual Override** requires uploading the primary Agent Tile and using specific trigger phrases to activate fallback mode.
  - **Phase 3: Restoration Loop** includes clearing threads, re-pasting startup content, and skipping small talk.

- **Common Errors and Fixes:**
  - “Who are you?” generic reply: Paste reseed and upload tile.
  - Tone drifts into generic assistant mode: Use “Fallback to [Name] mode”.
  - Assistant refuses command or ignores trigger: Manually re-inject agent + protocol.
  - Looping or recursive tone: Run `mythic_quarantine.py`.

## Notes
None.

---

## Connections

- [[index]]
- [[readme]]
- [[appendix-a-fieldguides]]
- [[appendix-b-masterindexes]]

## Sources

- [Appendix_E_ConversionRecovery.md](OBSIDIAN_VAULT/notes/insights/Appendix_E_ConversionRecovery.md)

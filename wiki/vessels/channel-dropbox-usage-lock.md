---
title: Channel Dropbox Usage Lock
domain: vessels
created: 2026-05-18
updated: 2026-07-22
sources: 
status: draft
tags: 
synthesized: 2026-05-19
synthesized_by: ollama/qwen2.5:7b
---

# Channel Dropbox Usage Lock

## Summary
The Channel Dropbox Usage Lock is a set of rules governing how the Dropbox connector can interact with Vault (ChatGPT) to ensure secure and controlled access.

## Key Points
- **Scope Restriction:** Interactions are limited to the `/AI/` path, with subdirectory access requiring explicit Operator permission.
- **Access Rules:**
  - No autonomous scanning; file discovery is by explicit filename or folder path given by the Operator.
  - No cross-folder access even if prompted.
  - All file operations require a clear, directed instruction.
  - Execution logs are required for every access request.

## Notes
None.

---

## Connections

- [[cacerts]]

## Sources

- [_Channel_Dropbox_Usage_Lock.md](OBSIDIAN_VAULT/notes/insights/_Channel_Dropbox_Usage_Lock.md)

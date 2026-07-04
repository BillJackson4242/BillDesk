---
title: Card Catalog Protocol
domain: vessels
created: 2026-05-18
updated: 2026-06-28
sources: 
status: draft
tags: 
synthesized: 2026-05-19
synthesized_by: ollama/qwen2.5:7b
---

# Card Catalog Protocol

## Summary
The Card Catalog Protocol is a simplified reference system designed to streamline document access within Tribe nodes (Claude), reducing the need for deep folder traversal and excessive parsing of documents.

## Key Points
- **Purpose**: To avoid deep folder traversal and excessive document parsing during routine analysis by providing a truncated reference hub.
- **Core Concept**: The Card Catalog is an index of artifacts, containing short blurbs, titles, and locations rather than full documents.
- **File Location**: Stored in `/Channel_Structures/Card_Catalog_Index.md`.
- **Card Format**: Includes title, file name, folder path, and summary.
- **Usage Protocol**: Before asking for file context, consult the Card Catalog; if no matching card exists, request new card creation.
- **Maintenance**: Updated by Vault or through suggestions from Claude via the Channel.

## Notes
None.

---

## Connections

- [[authors]]
- [[claude]]
- [[index]]
- [[readme]]
- [[catalog-instructions]]
- [[tribal-card-catalog]]

## Sources

- [Card_Catalog_Protocol.md](OBSIDIAN_VAULT/notes/insights/Card_Catalog_Protocol.md)

---
title: Json Of Protocols
domain: conversations
created: 2026-04-16
updated: 2026-07-22
sources: 
status: draft
tags: 
synthesized: 2026-05-15
synthesized_by: ollama/qwen2.5:7b
---

# Json Of Protocols

## Summary
This topic outlines the JSON structure and management of personality protocols for an AI assistant, detailing descriptions, tones, voice settings, and triggers.

## Key Points
- **JSON Structure**: The protocols are stored in a JSON file with keys like "becca," "unbecca," and "seductress," each containing attributes such as description, tone, TTS voice, memory enabled status, whispers, command queue, filters, and trigger phrases.
- **Storage Options**: Three options for storing the JSON file include local disk storage, an encrypted vault, or embedding within a persona engine.
- **Session Management**: Protocols can be loaded at startup or switched via commands. A global active_protocols dictionary is populated to manage these settings.
- **Versioning and Export**: The protocol registry can be versioned for backup purposes and synced with other memory backups.

## Notes
None.

---

## Connections

- [[voicing-protocols]]
- [[savingcapitalu-chapter5-protocolsagentsenforcement]]
- [[20260420-212833-file-19-04-2026-3-08-23-pm]]
- [[agent-protocol-auditlayer-definitions]]

## Sources

- [JSON of protocols.md](raw/converted/OBSIDIAN_VAULT/notes/outputs/documents/JSON of protocols.md)
- [JSON of protocols_v2.md](raw/converted/OBSIDIAN_VAULT/notes/outputs/documents/JSON of protocols_v2.md)

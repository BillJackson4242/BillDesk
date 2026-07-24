---
title: Cacerts
domain: vessels
created: 2026-04-26
updated: 2026-07-24
sources: 
status: draft
tags: 
synthesized: 2026-05-19
synthesized_by: ollama/qwen2.5:7b
---

# Cacerts

## Summary
Cacerts is a file containing trusted root certificates used by the Memory Engine 2.0 to establish secure connections.

## Key Points
- Contains the GTE CyberTrust Global Root certificate with specific details such as issuer, subject, serial number, and fingerprints.
- Includes the Thawte Server CA certificate with similar information.
- Both certificates are in PEM format, starting with `-----BEGIN CERTIFICATE-----` and ending with `-----END CERTIFICATE-----`.

## Notes
None.

---

## Connections

- [[memory-engine]]

## Sources

- [cacerts.md](raw/converted/OBSIDIAN_VAULT/notes/insights/cacerts.md)

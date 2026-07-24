---
title: 2026 07 04 Cowork U Reply Mcp Test
domain: memory
created: 2026-07-06
updated: 2026-07-24
sources:
  - raw/converted/Claude/Enhanced_Memory_System/memory_inbox/2026-07-04_cowork_u_reply_mcp_test.md
status: draft
tags:
  - memory
synthesized: 2026-07-24
synthesized_by: ollama/qwen2.5:7b
---

# 2026 07 04 Cowork U Reply Mcp Test

## Summary
This document outlines the results of a semantic search test and integration reply related to CoWork U's MCP (Memory Content Processing) test. The focus is on addressing issues with direct wiki queries, tunneling methods, and future architectural improvements.

## Key Points
- **Task Prompt Update:** Every run now includes a per-lane table detailing attempted, exported, failed, deferred/overflow, and error counts.
- **Direct Wiki Query Test Failure:** Fails due to connection refusal from the CoWork VM; localhost is interpreted as the Linux sandbox rather than the Windows host.
- **Tunnel/MCP Transport Verification:** Proven successful through browser context, but quick tunnels are unreliable for automation due to URL churn.
- **Architecture Recommendations:** Suggests using a stable named tunnel for regular queries and registering it as a custom connector in the DESKTOP app.
- **Scheduled Run Success:** First scheduled run completed successfully with 13 threads exported and no errors.

## Notes
None.

---

## Sources

- [2026-07-04_cowork_u_reply_mcp_test.md](raw/converted/Claude/Enhanced_Memory_System/memory_inbox/2026-07-04_cowork_u_reply_mcp_test.md)

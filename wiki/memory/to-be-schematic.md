---
title: To Be Schematic
domain: memory
created: 2026-05-05
updated: 2026-07-23
sources: 
status: draft
tags: 
synthesized: 2026-05-13
synthesized_by: ollama/qwen2.5:7b
---

# To Be Schematic

## Summary
The document outlines the target architecture for reorganizing Skills and Commands within BillDesk, focusing on principles and folder structure.

## Key Points
- **Operating Principles**: 
  - Skills hold procedures with tooling; Commands are thin invocations.
  - Shared content resides in `references/`, avoiding duplication.
  - Skill state is stored in memory, not within the skills themselves.
  - Grading and vault systems must communicate via `memory_inbox`.
  
- **Target Folder Structure**: 
  - `skills/` contains procedures and tooling, with specific subfolders like `grammar-mark/` and `rubric-assess/`.
  - `commands/` includes wrappers and utilities, such as `grade-prep.md` and new additions like `session-wrap.md`.
  - `references/` houses shared content to ensure consistency.

## Notes
None.

---

## Connections

- [[savingcapitalu-chapter9-filestrategy]]

## Sources

- [to-be-schematic.md](raw/converted/Claude/Enhanced_Memory_System/structured_context/to-be-schematic.md)

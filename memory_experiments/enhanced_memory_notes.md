# Enhanced Memory System Notes
*Created: 2026-01-23*
*Status: Exploring*

## Source
TikTok describing a 3-skill memory system for Claude Code

## The Three-Skill Approach

### Skill 1: Memory (Storage Structure)
- NOT a flat file - a **hierarchical folder tree**
- Branches get more specific as you go deeper
- Example structure:
  ```
  memory/
    personal/
      preferences/
      background/
    projects/
      teaching/
        engl150/
        engl211/
      coursework/
        pmgt320/
    technical/
      workflows/
      tools/
  ```
- Each leaf node could be a markdown file with specific memories

### Skill 2: REM Sleep (Automated Storage)
- Triggered at end of session (or manually)
- Deploys a **background subagent** that:
  1. Reads the conversation transcript
  2. Extracts key information worth remembering
  3. Decides WHERE in the memory tree it belongs
  4. Writes/updates the appropriate file(s)
- Runs in background so it doesn't interrupt workflow

### Skill 3: Recall (Automated Retrieval)
- Triggered at session start or when tackling new project
- Deploys a **background subagent** that:
  1. Takes context about current task/project
  2. Searches memory tree for relevant files
  3. Reads and summarizes relevant memories
  4. Passes them back to main Claude instance
- Prevents loading EVERYTHING when only some is relevant

## Comparison to Our Current Memento System

| Aspect | Memento (Current) | Three-Skill Approach |
|--------|-------------------|---------------------|
| Structure | Single flat file | Hierarchical tree |
| Storage | Manual updates | Automated via subagent |
| Retrieval | Load entire file at start | Selective search |
| Cross-platform | Works (GitHub) | Code U only (skills) |
| Complexity | Simple | "Very complicated" |
| Scalability | Gets unwieldy as it grows | Scales better |

## What We Could Implement

### Phase 1: Restructure Storage (Low effort)
Convert single file to folder structure:
```
BillDesk/
  memory/
    core.md              # Essential: identity, protocols, tone
    projects/
      engl150.md
      engl211.md
      pmgt320.md
    context/
      department.md
      career.md
    archive/
      completed.md
```
Still works with Claude App (just fetch multiple files or a combined one)

### Phase 2: Create /remember Skill (Medium effort)
Simple skill that:
- Prompts Claude to review recent conversation
- Asks what should be stored and where
- Updates appropriate memory file
- Pushes to GitHub

### Phase 3: Create /recall Skill (Medium effort)
Simple skill that:
- Takes project/topic context
- Searches memory folder for relevant files
- Loads only what's needed
- Could use Grep/Glob to find matches

### Phase 4: Background Automation (Higher effort)
- Auto-trigger remember at session end
- Auto-trigger recall at session start
- Requires hooks or careful skill design

## Claude Code Native Features (RESEARCHED 2026-01-23)

### 1. HOOKS - This is huge for automation

**Available hook points:**
- `SessionStart` - Fires when session begins OR resumes
- `SessionEnd` - Fires when session terminates
- `PreToolUse` / `PostToolUse` - Before/after any tool
- `UserPromptSubmit` - When you submit a prompt
- `Stop` - When Claude finishes responding
- `SubagentStop` - When a subagent completes

**Example SessionStart hook to auto-load memory:**
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/load-memory.sh"
          }
        ]
      }
    ]
  }
}
```

**Limitation:** Hooks are shell scripts - they can't directly inject into Claude's context. They write files or output to stderr.

### 2. SKILLS - Custom slash commands

**Creating /remember skill:**
```yaml
# ~/.claude/skills/remember/SKILL.md
---
name: remember
description: Save important context for future sessions
---

Save this to ~/.claude/persistent-memory.md with timestamp:

$ARGUMENTS
```

**Creating /recall skill:**
```yaml
---
name: recall
description: Load relevant memories for current project
---

Read and summarize relevant content from:
- ~/.claude/persistent-memory.md
- Project-specific memory files

Focus on: $ARGUMENTS
```

**Cool feature - dynamic context injection:**
```yaml
---
name: pr-review
---
## Context
- PR diff: !`gh pr diff`
- Comments: !`gh pr view --comments`
```
The `!`command`` syntax runs BEFORE Claude sees it - injects live data.

### 3. CLAUDE.md HIERARCHY - Built-in project memory

**Priority order (highest to lowest):**
1. Org-level managed policy
2. `.claude/CLAUDE.md` or `./CLAUDE.md` - Team shared
3. `.claude/rules/` folder - Modular topic rules
4. `~/.claude/CLAUDE.md` - Personal global prefs
5. `./CLAUDE.local.md` - Local only, auto-gitignored

**Imports work:**
```markdown
See @README for overview
@docs/coding-standards.md
@~/.claude/my-preferences.md
```

**Path-specific rules:**
```yaml
---
paths:
  - "src/api/**/*.ts"
---
# Only loads when working in API files
```

### 4. SUBAGENTS - Background processing

- Spawn with Task tool
- SubagentStop hook can access transcript at `agent_transcript_path`
- **Limitation:** Subagents don't automatically get parent conversation history

## What's Actually Possible Now

### Immediate wins we could implement:

1. **SessionStart hook** → Auto-run script that outputs memory summary
2. **/remember skill** → Quick way to save important stuff mid-session
3. **/recall skill** → Search and load relevant memories
4. **CLAUDE.md imports** → Memory file auto-loaded via `@claude_memory.md`
5. **SessionEnd hook** → Auto-trigger memory consolidation

### Architecture for Bill's setup:

```
~/.claude/
  settings.json          (already have this)
  CLAUDE.md              (global prefs + @imports memory)
  hooks/
    load-memory.sh       (SessionStart - outputs memory to context)
    save-memory.sh       (SessionEnd - consolidates session)
  skills/
    remember/SKILL.md    (/remember command)
    recall/SKILL.md      (/recall command)

BillDesk/
  claude_memory.md       (main memory - current system)
  memory/                (future: hierarchical)
    core.md
    projects/
    archive/
```

## Limitations Confirmed

1. Hooks can't directly inject into Claude's context (file/stdout only)
2. Subagents don't inherit parent conversation
3. No built-in persistent state between sessions
4. Skills can't hook into Claude's decision-making
5. **Claude App still can't use any of this** - Code U only

## Next Steps
1. [x] Research Claude Code hooks documentation
2. [ ] Create SessionStart hook to auto-load memory
3. [ ] Create /remember skill prototype
4. [ ] Create /recall skill prototype
5. [ ] Test if this plays nice with current GitHub-based system
6. [ ] Figure out Claude App fallback (maybe GitHub Actions?)

## Bill's Notes
*(Add observations here as we experiment)*


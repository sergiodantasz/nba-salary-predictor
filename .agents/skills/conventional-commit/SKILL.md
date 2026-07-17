---
name: conventional-commit
description: Add and commit changes using conventional commits
---

Create git commits for the current changes using the Conventional Commits standard.
When there are multiple semantically distinct changes, make **multiple commits** —
one per logical group.

## Context

Based on the conversation, determine what context is relevant for the commit
message. If the user provided specific guidance about what to commit or the
commit message, use that. Otherwise, analyze the changes to determine
appropriate commit messages.

## Process

1. **Analyze the changes** by running:
   - `git status` to see all modified/untracked files
   - `git diff` to see unstaged changes
   - `git diff --staged` to see already-staged changes
   - `git log --oneline -5` to see recent commit style

2. **Classify each changed file** into a change type by inspecting its diff:
   - **`style`** — diff is ONLY whitespace, formatting, or import reordering
   - **`docs`** — diff is ONLY comments or docstrings (no code changes)
   - **`refactor`** — diff renames symbols, extracts functions, moves code,
     or restructures without adding new behavior
   - **`fix`** — diff changes logic to correct incorrect behavior
   - **`feat`** — diff adds new fields, endpoints, parameters, or capabilities
   - If a file contains **mixed types** (e.g., both a style reformat AND a
     logic fix), split it into per-hunk changes using `git add -p` so each
     hunk lands in the appropriate commit.

3. **Group files by commit**:
   - Merge files of the same type that share a **common scope** into a single
     commit.
   - If two files have different types OR affect unrelated modules, they
     **must** go into separate commits.
   - Order commits so that `refactor` and `style` come **before** `feat` or
     `fix` (to keep history clean and reduce conflicts when bisecting).
   - If there is only one logical group, produce a **single commit**.

4. **For each group** (in order), do the following:

   a. **Stage the group's files** with `git add <file1> <file2> ...` or
      `git add -p <file>` for files with mixed hunks.

   b. **Determine the commit type** based on the group's classification:
      - `feat`: New feature or capability
      - `fix`: Bug fix
      - `docs`: Documentation only
      - `style`: Formatting, whitespace (not CSS)
      - `refactor`: Code restructuring without behavior change
      - `perf`: Performance improvement
      - `test`: Adding or updating tests
      - `build`: Build system or dependencies
      - `ci`: CI/CD configuration
      - `chore`: Maintenance tasks, tooling, config

   c. **Determine the scope** (optional):
      - Use a short identifier for the affected area: `feat(api):`, `fix(parser):`
      - Omit scope if changes are broad or it is unclear.

   d. **Write the commit message**:
      - **Subject line**: `<type>[<scope>]: <description>`
        - Use imperative mood ("add" not "added")
        - Lowercase, no period at end
        - Max 50 characters if possible, 72 hard limit
      - **Body** (if needed): Explain _why_, not _what_
        - Wrap at 72 characters
        - Separate from subject with a blank line

   e. **Commit** using a HEREDOC to pass the message.

## Commit Format

```
<type>[scope]: <subject>

[optional body explaining WHY this change was made]
```

## Examples

Single commit:

```
fix(parser): handle empty input without throwing
```

Two separate commits for style + feature:

```
$ git add -p api/app/main.py   # stage only reformat hunks
$ git commit -m "style(api): format docstrings and field declarations"

$ git add -p api/app/main.py   # stage remaining functional hunks
$ git add api/app/schemas.py
$ git commit -m "feat(api): add OpenAPI examples to request and response"
```

## Rules

- NEVER commit files that may contain secrets
- NEVER use `git commit --amend` unless the user explicitly requests it
- NEVER use `--no-verify` to skip hooks
- If the pre-commit hook fails, fix the issues and create a NEW commit
- If there are no changes to commit, inform the user and stop
- Use a HEREDOC to pass the commit message to ensure proper formatting

## Execute

Run the git commands to analyze, classify, group, stage, and commit the changes now.

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

2. **Classify changes at the hunk level**, not the file level. A single file
   may contain hunks of different types or hunks that are semantically related
   to changes in other files. Use `git diff` output to identify each hunk's
   purpose:
   - **`style`** — diff is ONLY whitespace, formatting, or import reordering
   - **`docs`** — diff is ONLY comments or docstrings (no code changes)
   - **`refactor`** — diff renames symbols, extracts functions, moves code,
     or restructures without adding new behavior
   - **`fix`** — diff changes logic to correct incorrect behavior
   - **`feat`** — diff adds new fields, endpoints, parameters, or capabilities
   - Prefer **partial staging** (`git add -p`) over whole-file staging so
     each hunk lands in its most appropriate commit, even when no single file
     contains mixed types.

3. **Group hunks into commits by semantic relationship**:
   - Merge hunks of the same type that share a **common scope** into a single
     commit, regardless of which file they come from.
   - If two hunks have **different types** or affect **unrelated modules**,
     they **must** go into separate commits — even if they are in the same
     file.
   - Order commits so that `refactor` and `style` come **before** `feat` or
     `fix` (to keep history clean and reduce conflicts when bisecting).
   - If there is only one logical group, produce a **single commit**.

4. **For each group** (in order), do the following:

   a. **Stage the group's hunks** using `git add -p <file>` for each file
      that contains relevant hunks. Stage whole files with `git add <file>`
      only when every hunk in the file belongs to the same group.

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

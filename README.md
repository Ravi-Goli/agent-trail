# Agent Trail

[![Test](https://github.com/Ravi-Goli/agent-trail/actions/workflows/test.yml/badge.svg)](https://github.com/Ravi-Goli/agent-trail/actions/workflows/test.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)

Local-first activity trail for AI-assisted coding sessions.

Context tools help an agent start with better information. Agent Trail focuses on the other side of the workflow: what the agent changed, which commands ran, what failed, what passed, and what should go into the handoff or PR description.

## Why this exists

AI coding sessions can move quickly. After a few prompts, it is easy to lose the thread:

- Which files changed?
- Which tests actually ran?
- What decisions were made?
- What risks remain?
- What should reviewers look at first?

Agent Trail records those events locally and turns them into a clean Markdown timeline.

## Features

- Start named coding sessions
- Record notes, decisions, risks, and next steps
- Run and capture command output
- Snapshot git status and diff stats
- Generate session summaries
- Export PR notes from the session timeline
- Stores everything locally in `.agent-trail/`

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

agent-trail init
agent-trail start "fix login token refresh"
agent-trail note "Found token refresh logic in src/auth/session.ts"
agent-trail run -- npm test
agent-trail snapshot
agent-trail summary
agent-trail export-pr-notes --output PR_NOTES.md
```

## Install From GitHub

```bash
pip install "git+https://github.com/Ravi-Goli/agent-trail.git"
```

## Run Tests

```bash
pip install -e ".[dev]"
pytest -q
```

## Example Summary

```md
# Agent Trail Summary

Goal: fix login token refresh

## Commands
- PASS `npm test`

## Changed Files
- src/auth/session.ts
- tests/auth/session.test.ts

## Notes
- Found token refresh logic in src/auth/session.ts
- Added regression coverage for expired access tokens

## Risks
- Refresh-token rotation still needs integration coverage
```

## Commands

```bash
agent-trail init
agent-trail start "describe the goal"
agent-trail note "important observation"
agent-trail decision "use retry budget instead of infinite retries"
agent-trail risk "integration coverage still missing"
agent-trail next-step "add e2e test for refresh-token rotation"
agent-trail run -- pytest -q
agent-trail snapshot
agent-trail summary
agent-trail export-pr-notes --output PR_NOTES.md
```

## Suggested GitHub Topics

`ai` `developer-tools` `cli` `python` `git` `agentops` `ai-coding` `productivity`

## Roadmap

- GitHub PR body generation from a branch diff
- Detection of stale sessions
- HTML timeline export
- Optional MCP server interface
- Repeated-review-pattern tracking

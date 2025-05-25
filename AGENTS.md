# AGENTS.md

# LynseDB Contributor & Agent Guide

## Overview

This repository is for **LynseDB**, a Python-based system targeting compatibility with Python 3.13+ and modern development practices.  
All agents (human or Codex) must adhere to the instructions below to ensure maintainability, correctness, and continuity across tasks.

---

## Target Environment

- **Python version:** 3.13+ (use `python --version` to confirm)
- All tasks, code, and scripts must run and pass in this environment.
- If a dependency or tool does not support Python 3.13+, document the issue in `NOTES.md` and propose alternatives.

---

## File & Folder Boundaries

- **Core code:** Resides under `/src` (or as otherwise documented in README.md). Do not scatter core logic elsewhere.
- **Tests:** Under `/tests` or as specified in `pytest.ini`. All new logic requires corresponding tests.
- **Documentation:** Use `/docs` for persistent documentation; use `NOTES.md` for ephemeral/working memory (see below).
- **Config:** Version all critical config in the repo (e.g., `.pre-commit-config.yaml`, `pyproject.toml`, `requirements.txt`).

---

## Working Memory (`NOTES.md` Protocol)

- `NOTES.md` serves as the **ephemeral, agent-managed working memory**.
- **Codex agents are required to append to and maintain `NOTES.md`** at the end of each major task or as new tools, limitations, or ideas emerge.
- Use clear Markdown bullets or sections for:
    - Tooling wishes and rationale.
    - Known issues or environment constraints.
    - Discovered patterns, design insights, or technical debt.
    - TODOs or follow-up actions that do not warrant an issue yet.
- Do **not** use `NOTES.md` for final documentation; migrate stable insights to `/docs` or relevant files as appropriate.

---

## Required Tools & Validation

The following tools must be installed, configured, and used in all CI and local workflows:

- **pre-commit:** Linting/formatting checks before every commit.
- **pytest:** For all unit/integration tests.
- **pytest-cov:** Test coverage reporting (target: ≥90% for all new modules).
- **pytest-xdist:** Parallelized test execution (use `-n auto`).
- **bandit:** Static code security analysis.
- **ipykernel, jupyter:** For notebook-based experimentation; not required for headless CI.
- **mkdocs-material:** Documentation generation; update `/docs` when relevant changes are made.

Validation steps for every PR or agent change:

1. Run `pre-commit run --all-files` and confirm all checks pass.
2. Run `pytest --cov=src --cov-report=term-missing` and confirm 100% pass rate, target coverage ≥90%.
3. Run `bandit -r src/` and confirm no high-severity issues.
4. Update `NOTES.md` with any tool or environment adjustments after every major change.
5. If a new tool is installed, or an old one removed, **document the reasoning in `NOTES.md`**.

---

## Style & Contribution Guidelines

- **Code style:** Enforced by `pre-commit` and project linter configuration (`pyproject.toml`, `.flake8`, etc.).
- **Typing:** Use type annotations everywhere possible.
- **Tests:** All new code must be accompanied by tests, preferably using `pytest` idioms.
- **Docs:** Update `/docs` for finalized docs; use inline comments for non-obvious logic; keep `NOTES.md` in sync with ongoing agent insights.
- **Commits & PRs:** 
    - Commit messages must be clear, imperative, and reference affected modules.
    - PR titles: `[lynsedb] <short, descriptive title>`
    - Each PR should reference the relevant section(s) of this `AGENTS.md` and describe **how validation was performed**.
    - Run `pre-commit`, `pytest`, and `bandit` before opening a PR.

---

## Directory-Specific Instructions

- **/src/**: All business logic, strictly type-annotated, must pass lint and security checks.
- **/tests/**: Mirrored structure to `/src/`, no test left behind.
- **/docs/**: Only stable documentation; do not migrate "notes" until stabilized.
- **/notebooks/**: Allowed for experimentation only; code must be ported to `/src/` for production.
- **/scripts/**: Use only for devtools, migrations, or reproducible experiments.

---

## Task Execution & Agent Instructions

- **Always check for the latest `AGENTS.md` and `NOTES.md` before starting any task.**
- Before making changes, confirm tool versions and environment.
- If an issue is found with Python 3.13+ compatibility, document it in `NOTES.md` and, if blocking, open an issue.
- Update `NOTES.md` as a running log: summarize what was done, new constraints, blockers, and next steps.
- When adding new dependencies, confirm:
    - They are compatible with Python 3.13+.
    - They are not deprecated.
    - They do not introduce high/critical security vulnerabilities.
    - Record any caveats or observations in `NOTES.md`.

---

## Continuous Improvement

- Agents (human or Codex) are expected to treat `NOTES.md` as the canonical scratchpad.
- When a pattern stabilizes, migrate it to `/docs` or incorporate it into `AGENTS.md`.
- All changes that affect agent workflow, tool usage, or repo conventions must be reflected in this file and referenced in future PRs.

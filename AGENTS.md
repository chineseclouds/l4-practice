# AGENTS.md

Guidance for coding agents (Claude Code, Codex, etc.) working in this repository.

## Project
- `l4tools.py`: small pure-Python utility functions.
- `tests/`: pytest tests. Every public function must have tests.

## Setup and tests
- Python 3.12. Run tests with `uv run --with pytest pytest -q`
  (or `python -m pytest -q` in a virtual environment with pytest installed).
- CI (GitHub Actions, job `test`) runs `pytest -q` on every pull request and must pass before merge.

## Workflow rules
- Never push to `main`; it is protected. Work on a branch named `<type>/<short-topic>`,
  for example `feat/char-count` or `chore/bump-actions`.
- Keep each pull request small and focused on one issue. Reference it in the PR body (`Closes #N`).
- Add or update tests for every behavior change. Run the tests locally before pushing when possible.
- Do not modify `.github/workflows/` or `AGENTS.md` unless the issue asks for it.
- Do not add dependencies without explaining why in the PR body.
- Never commit secrets, tokens or personal data.
- Do not merge your own pull request; the repository owner reviews and merges.

## Pull request description
State what changed, why, how it was tested (commands and results), and anything left undone.
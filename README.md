# OSS Health

[![CI](https://github.com/MaxenceBoucquez/oss-health/actions/workflows/ci.yml/badge.svg)](https://github.com/MaxenceBoucquez/oss-health/actions/workflows/ci.yml)

**A dependency-free, actionable health audit for open-source repositories.**

Most repository audits stop at “you are missing a README”. OSS Health produces a score, grade, machine-readable JSON, Markdown reports, CI exit codes, and security filename warnings in a few seconds.

## Quick start

```bash
# No installation required
python -m oss_health /path/to/repository

# Markdown report for an issue or client hand-off
python -m oss_health . --format markdown > OSS_HEALTH.md

# JSON for CI, dashboards, or an AI agent
python -m oss_health . --format json > oss-health.json

# Fail CI until all baseline checks pass
python -m oss_health . --strict
```

With the package installed:

```bash
pip install .
oss-health . --strict
```

## What it checks

- README and project onboarding
- License
- Contributing guide
- GitHub Actions CI
- Test directory
- Dependency manifest
- Security policy
- Code of conduct
- Suspicious filenames such as `.env`, credentials, tokens, or private keys

Example output:

```text
OSS Health: 75/100 (grade B)
PASS  README
PASS  License
WARN  Security policy — Tell users how to report vulnerabilities
WARN  Code of conduct — Set expectations for a welcoming project
```

## Why this exists

A healthy OSS project converts more visitors into users and contributors. This tool is intentionally small enough to run locally, in CI, or as part of an AI coding workflow without sending source code anywhere.

## Paid maintainer service

I also provide focused human help for projects that want to improve their score:

- **€9 — Snapshot:** written report with the top three improvements
- **€29 — Fix plan:** report plus PR-ready implementation plan
- **€79 — Fix sprint:** implementation of the highest-impact baseline fixes

Payment: [PayPal](https://www.paypal.com/qrcodes/p2pqrc/Y8W5GZNGGTLFQ)

Include the repository URL and the selected package in the PayPal note. Never send credentials, tokens, or private source code through the payment note.

## Development

```bash
python -m unittest discover -s tests -v
python -m oss_health . --strict
```

## License

MIT

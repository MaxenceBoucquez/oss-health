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

## Free tool, paid outcome

The CLI is intentionally free and open source. You should not pay to run it.

The paid offer is for work around the tool that cannot be automated safely or usefully:

- **€9 — Public snapshot:** human-written prioritization of the top three improvements on a public repository
- **€29 — Private audit:** review of a private repository, with an actionable report and maintainer questions
- **€79 — Fix sprint:** implementation of the highest-impact baseline fixes in a pull request
- **€149 — AI/OSS launch pack:** repository audit, contributor onboarding, CI hardening, and a release-readiness checklist

You are paying for private context, judgment, implementation, and time saved — not for the CLI binary.

Payment: [PayPal](https://www.paypal.com/qrcodes/p2pqrc/Y8W5GZNGGTLFQ)

Include the repository URL and the selected package in the PayPal note. Never send credentials, tokens, or private source code through the payment note.

## Development

```bash
python -m unittest discover -s tests -v
python -m oss_health . --strict
```

## License

MIT

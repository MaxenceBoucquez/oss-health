# OSS Health

A tiny, dependency-free CLI that checks whether an open-source repository is ready for contributors and users.

## Use

```bash
python -m oss_health /path/to/repo
```

It checks for a README, license, contribution guide, issue templates, CI, tests, dependency manifests, and obvious secret filenames. It exits with code `1` when important basics are missing, making it useful in CI.

## Paid help

Need a fast, human review of your project? I offer a focused OSS/AI developer audit:

- **€9** — written 10-minute health report
- **€29** — report + concrete PR-ready fixes
- **€79** — implementation of the highest-impact fixes

Payment: [PayPal](https://www.paypal.com/qrcodes/p2pqrc/Y8W5GZNGGTLFQ)

Send the repository URL and the selected amount in the PayPal note. No credentials are required.

## License

MIT

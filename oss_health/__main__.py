"""Actionable repository health audits, with zero runtime dependencies."""
from pathlib import Path
import argparse, json, sys

VERSION = "0.2.0"

def scan(repo: Path) -> dict:
    repo = repo.resolve()
    names = {p.name.lower() for p in repo.iterdir()} if repo.is_dir() else set()
    def exists(*candidates): return any((repo / c).exists() for c in candidates)
    checks = [
        ("README", any(n.startswith("readme") for n in names), "Explain the problem, setup, usage, and limitations"),
        ("License", any(n.startswith(("license", "copying")) for n in names), "Add an OSI-approved license"),
        ("Contributing guide", any(n.startswith("contribut") for n in names), "Add CONTRIBUTING.md with a first-contribution path"),
        ("CI workflow", (repo/'.github'/'workflows').is_dir() and any((repo/'.github'/'workflows').iterdir()), "Add a reproducible CI workflow"),
        ("Tests", (repo/'tests').is_dir() or (repo/'test').is_dir(), "Add tests that contributors can run locally"),
        ("Dependency manifest", exists('pyproject.toml','setup.py','package.json','go.mod','Cargo.toml','requirements.txt'), "Declare dependencies and supported runtimes"),
        ("Security policy", exists('SECURITY.md','.github/SECURITY.md'), "Tell users how to report vulnerabilities"),
        ("Code of conduct", exists('CODE_OF_CONDUCT.md','.github/CODE_OF_CONDUCT.md'), "Set expectations for a welcoming project"),
    ]
    suspicious = sorted(n for n in names if any(x in n for x in ('.env', 'id_rsa', 'credentials', 'secret', 'token')) and n not in ('.env.example',))
    passed = sum(ok for _, ok, _ in checks)
    score = round(100 * passed / len(checks))
    return {'repo': str(repo), 'score': score, 'passed': passed, 'total': len(checks),
            'checks': [{'name': n, 'passed': ok, 'advice': advice} for n, ok, advice in checks],
            'security_flags': suspicious, 'grade': 'A' if score >= 90 and not suspicious else 'B' if score >= 70 and not suspicious else 'C' if score >= 50 else 'D'}

def markdown(report):
    lines=["# OSS Health report", f"**Score: {report['score']}/100 · Grade {report['grade']}**", "", "## Checks"]
    lines += [f"- {'✅' if x['passed'] else '⚠️'} **{x['name']}**" + ('' if x['passed'] else f" — {x['advice']}") for x in report['checks']]
    if report['security_flags']: lines += ["", "## Security flags", *[f"- `{x}`" for x in report['security_flags']]]
    return '\n'.join(lines) + '\n'

def text(report):
    lines=[f"OSS Health: {report['score']}/100 (grade {report['grade']})"]
    lines += [("PASS" if x['passed'] else "WARN") + f"  {x['name']}" + ('' if x['passed'] else f" — {x['advice']}") for x in report['checks']]
    if report['security_flags']: lines.append('SECURITY ' + ', '.join(report['security_flags']))
    return '\n'.join(lines) + '\n'

def main(argv=None):
    p=argparse.ArgumentParser(description='Audit an open-source repository and produce actionable fixes')
    p.add_argument('repo', nargs='?', default='.')
    p.add_argument('--format', choices=('text','json','markdown'), default='text')
    p.add_argument('--strict', action='store_true', help='exit 1 unless every check passes and no security flags exist')
    p.add_argument('--version', action='version', version=VERSION)
    args=p.parse_args(argv)
    report=scan(Path(args.repo))
    print(json.dumps(report, indent=2) if args.format=='json' else markdown(report) if args.format=='markdown' else text(report), end='')
    return 1 if args.strict and (report['score'] < 100 or report['security_flags']) else 0

if __name__ == '__main__': raise SystemExit(main())

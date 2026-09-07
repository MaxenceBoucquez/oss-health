from pathlib import Path
import sys


def check(repo: Path):
    files = {p.name.lower() for p in repo.iterdir()} if repo.exists() else set()
    checks = [
        ("README", any(n.startswith("readme") for n in files), "Explain what the project does and how to run it"),
        ("License", any(n.startswith("license") or n.startswith("copying") for n in files), "Add an OSI-approved license"),
        ("Contributing guide", any(n.startswith("contribut") for n in files), "Add CONTRIBUTING.md"),
        ("CI workflow", (repo/'.github'/'workflows').is_dir() and any((repo/'.github'/'workflows').iterdir()), "Add a GitHub Actions workflow"),
        ("Tests", any(n in files for n in ("tests", "test")) or (repo/'tests').is_dir(), "Add an executable test suite"),
        ("Dependency manifest", any(n in files for n in ("pyproject.toml", "package.json", "go.mod", "cargo.toml", "requirements.txt")), "Declare dependencies explicitly"),
    ]
    suspicious = sorted(n for n in files if any(x in n for x in (".env", "id_rsa", "credentials", "secret")))
    passed = sum(ok for _, ok, _ in checks)
    print(f"OSS Health: {passed}/{len(checks)} checks passed")
    for label, ok, advice in checks:
        print(("PASS" if ok else "WARN") + f"  {label}" + ("" if ok else f" — {advice}"))
    if suspicious:
        print("WARN  Suspicious filenames: " + ", ".join(suspicious))
    return 0 if passed == len(checks) and not suspicious else 1


if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    raise SystemExit(check(target))

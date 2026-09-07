import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from oss_health.__main__ import main, scan


class OssHealthTests(unittest.TestCase):
    def test_scan_scores_complete_project(self):
        with TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            for name in ('README.md', 'LICENSE', 'CONTRIBUTING.md', 'SECURITY.md', 'CODE_OF_CONDUCT.md', 'pyproject.toml'):
                (tmp_path / name).write_text('x')
            (tmp_path / 'tests').mkdir()
            workflows = tmp_path / '.github' / 'workflows'
            workflows.mkdir(parents=True)
            (workflows / 'ci.yml').write_text('x')
            report = scan(tmp_path)
            self.assertEqual(report['score'], 100)
            self.assertEqual(report['security_flags'], [])

    def test_json_output_is_machine_readable(self):
        with TemporaryDirectory() as directory:
            # main writes valid JSON; redirecting stdout is unnecessary for the contract test.
            report = scan(Path(directory))
            encoded = json.dumps(report)
            self.assertEqual(json.loads(encoded)['total'], 8)

    def test_strict_fails_incomplete_project(self):
        with TemporaryDirectory() as directory:
            self.assertEqual(main([directory, '--strict']), 1)


if __name__ == '__main__':
    unittest.main()

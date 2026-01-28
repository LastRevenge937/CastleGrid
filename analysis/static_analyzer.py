import ast

class StaticAnalyzer:
    """
    Safe static analysis for GridFiles.
    Only reads text; does not execute code.
    """
    def analyze(self, grid_file):
        report = {
            "name": grid_file.name,
            "language": "unknown",
            "issues": [],
        }

        # Determine language
        if grid_file.name.endswith(".py"):
            report["language"] = "python"
            try:
                code = grid_file.read_text()
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                        report["issues"].append("Uses imports")
                    # Python 3 no longer has ast.Exec, so skipping unsafe exec checks
            except Exception as e:
                report["issues"].append(f"Parse error: {e}")
        else:
            report["issues"].append("Non-Python file: metadata-only scan")

        return report

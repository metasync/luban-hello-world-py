import importlib.metadata
import re
from pathlib import Path


def get_version() -> str:
    # 1. Try to get version from installed package metadata
    try:
        return importlib.metadata.version("luban-hello-world-py")
    except importlib.metadata.PackageNotFoundError:
        pass

    # 2. Fallback: Read from pyproject.toml using regex (to support older Python without tomllib)
    try:
        pyproject_path = Path(__file__).parent / "pyproject.toml"
        if pyproject_path.exists():
            content = pyproject_path.read_text(encoding="utf-8")
            # Look for version = "..." under [project]
            # This is a simplified parser but works for standard pyproject.toml
            project_section = re.search(r'\[project\](.*?)(?=\n\[|$)', content, re.DOTALL)
            if project_section:
                version_match = re.search(r'^version\s*=\s*["\']([^"\']+)["\']', project_section.group(1), re.MULTILINE)
                if version_match:
                    return version_match.group(1)
    except Exception:
        pass

    return "0.0.0"


__version__ = get_version()

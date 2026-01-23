import importlib.metadata
from pathlib import Path
import subprocess


def read_pyproject_version():
    try:
        import tomllib
        pyproject = Path(__file__).with_name("pyproject.toml")
        if pyproject.exists():
            with pyproject.open("rb") as f:
                data = tomllib.load(f)
            return data.get("project", {}).get("version")
    except Exception:
        return None


def get_version() -> str:
    try:
        return importlib.metadata.version("luban-hello-world-py")
    except importlib.metadata.PackageNotFoundError:
        try:
            result = subprocess.run(
                ["git", "describe", "--tags", "--dirty", "--always"],
                cwd=Path(__file__).parent,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                check=False,
            )
            v = result.stdout.strip()
            if v:
                return v
        except Exception:
            pass
        pv = read_pyproject_version()
        if pv:
            return pv
        return "0.0.0"


__version__ = get_version()

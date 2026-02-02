## Implementation Steps

### 1. Create Directory Structure
- Create `src/luban_hello_world_py/`.
- Create `src/luban_hello_world_py/__init__.py`.

### 2. Move Source Files
- Move `main.py` and `version.py` to `src/luban_hello_world_py/`.

### 3. Update version.py
- Update `get_version()` to look for `pyproject.toml` at `Path(__file__).parent.parent.parent / "pyproject.toml"`.

### 4. Update pyproject.toml
- Update `[project.scripts]` to `app = "luban_hello_world_py.main:start"`.
- Update `[tool.hatch.build.targets.wheel]` packages to `["src/luban_hello_world_py"]`.

### 5. Finalize and Push
- Verify locally: `uv run app`.
- Commit the restructure and update the remote `main` branch and `v0.1.0` tag.

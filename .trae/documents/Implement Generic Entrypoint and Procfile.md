## Implementation Steps

### 1. Update main.py
- Update `read_root()` to use `os.environ.get("GREETING", "Hello")` for the message.
- Add `start()` function to handle `PORT` (default 8080) and launch the server.
- Ensure `import os` is present.

### 2. Configure pyproject.toml
- Add `[project.scripts]` with `app = "main:start"`.

### 3. Create Procfile
- Set `web: uv run app`.

### 4. Finalize and Push
- Verify locally: `GREETING="Hi" PORT=9000 uv run app`.
- Commit changes and update the remote `main` branch and `v0.1.0` tag.

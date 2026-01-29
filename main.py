from fastapi import FastAPI
import sys
import os
from version import __version__

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from Luban CI Sample App!",
        "python_version": sys.version,
        "version": __version__,
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

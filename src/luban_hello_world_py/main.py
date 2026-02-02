from fastapi import FastAPI
import sys
import os
from .version import __version__

app = FastAPI()


@app.get("/")
def read_root():
    greeting = os.environ.get("GREETING", "Hello")
    return {
        "message": f"{greeting} from Luban CI Sample App!",
        "python_version": sys.version,
        "version": __version__,
    }


def start():
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("luban_hello_world_py.main:app", host="0.0.0.0", port=port)


if __name__ == "__main__":
    start()

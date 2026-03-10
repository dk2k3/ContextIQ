import subprocess
import sys

print("Starting ContextIQ Backend (FastAPI)...")

backend = subprocess.Popen(
    ["uvicorn", "app.api.server:app", "--reload"]
)

print("Starting ContextIQ Frontend (Streamlit)...")

frontend = subprocess.Popen(
    ["streamlit", "run", "ui/app.py"]
)

try:
    backend.wait()
    frontend.wait()
except KeyboardInterrupt:
    print("Shutting down ContextIQ...")
    backend.terminate()
    frontend.terminate()
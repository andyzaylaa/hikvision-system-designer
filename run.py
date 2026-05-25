"""
HikDesigner AI - One-click launcher
Run this file to start the app: python run.py
Then open http://localhost:8000 in your browser.
"""
import subprocess
import sys
import os

def main():
    backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend")
    os.chdir(backend_dir)

    # Check if dependencies are installed
    try:
        import uvicorn  # noqa: F401
    except ImportError:
        print("Installing dependencies... (first time only, please wait)")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])

    print()
    print("=" * 50)
    print("  HikDesigner AI is starting...")
    print("  Open your browser to: http://localhost:8000")
    print("  Press Ctrl+C to stop")
    print("=" * 50)
    print()

    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()

"""
post_gen_prompt.py
Ian Kollipara <ian.kollipara@gmail.com>
2024-11-30

Post Generation Setup
"""

import os
import pathlib
import secrets

os.system("uv sync")
os.system("npm i --include-dev")

with open(".env", "w+") as f:
    f.write(f"SECRET_KEY={secrets.token_urlsafe(32)}\n")
    f.write("DEBUG=true\n")
    f.write("ALLOWED_HOSTS=\n")
    f.write("INTERNAL_IPS=127.0.0.1\n")
    f.write("LOG_LEVEL=DEBUG\n")
    f.write("EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'\n")
    f.write("DATABASE_URL='sqlite:///db.sqlite3'\n")
    f.write("PYTHONBREAKPOINT=ipdb.set_trace\n")
    f.write("HUEY_NUM_WORKERS=1\n")
    f.write("HUEY_WORKER_CLASS='huey.SqliteHuey'\n")
    f.write("HUEY_DBNAME='huey.db'\n")
    f.write("HUEY_WORKER_TYPE='thread'\n")
    f.write("HUEY_ENABLE_PERIODIC=true\n")

with open(".env.testing", "w+") as f:
    f.write("DEBUG=false\n")
    f.write("ALLOWED_HOSTS=\n")
    f.write("INTERNAL_IPS=127.0.0.1\n")
    f.write("LOG_LEVEL=DEBUG\n")
    f.write("DATABASE_URL='sqlite:///:inmemory:'\n")
    f.write("PYTHONBREAKPOINT=ipdb.set_trace\n")
    f.write("HUEY_NUM_WORKERS=1\n")
    f.write("HUEY_WORKER_CLASS='huey.SqliteHuey'\n")
    f.write("HUEY_DBNAME='huey.db'\n")
    f.write("HUEY_WORKER_TYPE='thread'\n")
    f.write("HUEY_ENABLE_PERIODIC=true\n")

os.system("just migrate")
os.system("git init")
pathlib.Path(".gitignore").write_text(
    ".venv\n" "node_modules\n" ".env\n" "__pycache__/\n"
)
os.system("git add .")
os.system("git commit -m ':sparkles: Initial Commit'")
os.system("git checkout -b develop")

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
    f.write(
        'STORAGES_BACKEND="whitenoise.storage.CompressedManifestStaticFilesStorage"\n'
    )

with open(".env.testing", "w+") as f:
    f.write("DEBUG=false\n")
    f.write("ALLOWED_HOSTS=\n")
    f.write("INTERNAL_IPS=127.0.0.1\n")
    f.write("LOG_LEVEL=DEBUG\n")
    f.write("DATABASE_URL='sqlite:///:inmemory:'\n")
    f.write("PYTHONBREAKPOINT=ipdb.set_trace\n")
    f.write('STORAGES_BACKEND="django.core.files.storage.FileSystemStorage"\n')

os.system("direnv allow")
os.system("git init")
pathlib.Path(".gitignore").write_text(
    ".venv\nnode_modules\n.env\n__pycache__/\nstatic/dist\nmedia/\n"
)
pathlib.Path("static/dist").mkdir(parents=True, exist_ok=True)
os.system("git add .")
os.system("git commit -m ':sparkles: Initial Commit'")
os.system("git checkout -b develop")

create_remote = input("Create remote on GitHub [y/n]: ")
if create_remote.lower() == "y":
    os.system("gh repo create")

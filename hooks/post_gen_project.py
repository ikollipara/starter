"""
post_gen_prompt.py
Ian Kollipara <ian.kollipara@gmail.com>
2024-11-30

Post Generation Setup
"""

import os
import pathlib
import secrets

os.system("mise install")
os.system("uv sync")
os.system("npm i")

os.system(f"mise set SECRET_KEY={secrets.token_urlsafe(32)}")

if "{{ cookiecutter.database }}" == "postgres":
    os.system("rm -rf ./docker/mysql")
elif "{{ cookiecutter.database }}" == "mysql":
    os.system("rm -rf ./docker/postgres")
else:
    os.system("rm -rf ./docker")

if (
    "{{ cookiecutter.email}}" == "console"
    and "{{ cookiecutter.database}}" == "sqlite"
):
    os.system('rm -rf docker-compose.yml')

os.system("git init")
pathlib.Path(".gitignore").write_text(
    ".venv\nnode_modules\n.env\n__pycache__/\nstatic/dist\nmedia/\n.docker/\n"
)
pathlib.Path("static/dist").mkdir(parents=True, exist_ok=True)
os.system("git add .")
os.system("git commit -m ':sparkles: Initial Commit'")
os.system("git checkout -b develop")

create_remote = input("Create remote on GitHub [y/n]: ")
if create_remote.lower() == "y":
    os.system("gh repo create")

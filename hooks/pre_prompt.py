"""
pre_prompt.py
Ian Kollipara <ian.kollipara@gmail.com>
2024-11-30

PrePrompt Scripting
"""

import enum
import io
import platform
import shutil
import sys
import typing

RESET = "\033[0m"

__version__ = "0.0.1"


class Color(enum.StrEnum):
    BLACK = "30"
    RED = "31"
    GREEN = "32"
    YELLOW = "33"
    BLUE = "34"
    PURPLE = "35"
    CYAN = "36"
    WHITE = "37"


class Modifier(enum.StrEnum):
    FG = "0;"
    BOLD = "1;"
    UNDERLINE = "4;"
    BG = ""


def write(
    s: typing.AnyStr = "",
    color: Color = Color.WHITE,
    modifier: Modifier = Modifier.BG,
    writer: io.IOBase = sys.stdout,
):
    writer.write(f"\033[{modifier.value}{color.value}m{s}{RESET}\n")


write(
    "███████╗████████╗ █████╗ ██████╗ ████████╗███████╗██████╗ \n"
    "██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗\n"
    "███████╗   ██║   ███████║██████╔╝   ██║   █████╗  ██████╔╝\n"
    "╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗\n"
    "███████║   ██║   ██║  ██║██║  ██║   ██║   ███████╗██║  ██║\n"
    "╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝",
    Color.BLUE,
    Modifier.BOLD,
)
write("An opinionated Django Bootstrapper", Color.CYAN, Modifier.BOLD)
write("By Ian Kollipara <ian.kollipara@gmail.com>", Color.WHITE, Modifier.BOLD)
write(f"Version {__version__}")
write("----------------------------------------------------------")
write()
write()


### Checks ###

if sys.version_info.minor < 12:
    write(
        f"Invalid Python Version ({platform.python_version()} < 3.12)",
        Color.RED,
        writer=sys.stderr,
    )
    exit(1)

if not shutil.which("uv"):
    write("UV is not installed. Please install UV", Color.RED, writer=sys.stderr)
    exit(1)

if not shutil.which("node") or not shutil.which("npm"):
    write(
        "Node and NPM are not installed. Please install Node and NPM",
        Color.RED,
        writer=sys.stderr,
    )
    exit(1)

if not shutil.which("just"):
    write("Just is not installed. Please install Just.", Color.RED, writer=sys.stderr)
    exit(1)

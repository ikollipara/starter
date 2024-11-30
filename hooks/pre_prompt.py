"""
pre_prompt.py
Ian Kollipara <ian.kollipara@gmail.com>
2024-11-30

PrePrompt Scripting
"""

import enum
import io
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

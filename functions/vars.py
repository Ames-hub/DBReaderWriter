colours = {
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[1;34m",
    "purple": "\033[1;35m",
    "cyan": "\033[1;36m",
    "white": "\033[1;37m",
    "gray": "\033[1;38m",
    "black": "\033[1;30m",
    "reset": "\033[0;0m"
}

import os
def clear_console(): os.system("cls" if os.name == "nt" else "clear")
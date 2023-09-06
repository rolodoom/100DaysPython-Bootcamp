import platform
import os


def clear():
    """Clears the screen"""
    system = platform.system().lower()
    if system == "linux" or system == "darwin":
        os.system("clear")
    elif system == "windows":
        os.system("cls")


def logo():
    """Prints the logo"""
    logo = """╔══════════════════════════════════════════════════╗
║      ╔╗╔┌─┐┌┬┐┌─┐  ╔═╗┬  ┌─┐┬ ┬┌─┐┌┐ ┌─┐┌┬┐      ║
║      ║║║├─┤ │ │ │  ╠═╣│  ├─┘├─┤├─┤├┴┐├┤  │       ║
║      ╝╚╝┴ ┴ ┴ └─┘  ╩ ╩┴─┘┴  ┴ ┴┴ ┴└─┘└─┘ ┴       ║
╠══════════════════════════════════════════════════╣
║ (International) Radiotelephony Spelling Alphabet ║
╚══════════════════════════════════════════════════╝
"""
    print(logo)

import platform
import os
from time import sleep


def clear():
    """Clears the screen"""
    system = platform.system().lower()
    if system == "linux" or system == "darwin":
        os.system("clear")
    elif system == "windows":
        os.system("cls")


def logo():
    """Prints the logo"""
    logo = """         ╔════════════════════════════════════════════╗        
  ;)( ;  ║  ╔═╗┌─┐┌─┐┌─┐┌─┐┌─┐   ╔╦╗┌─┐┌─┐┬ ┬┬┌┐┌┌─┐  ║   ;)( ;
 :----:  ║  ║  │ │├┤ ├┤ ├┤ ├┤    ║║║├─┤│  ├─┤││││├┤   ║  :----:
C|====|  ║  ╚═╝└─┘└  └  └─┘└─┘   ╩ ╩┴ ┴└─┘┴ ┴┴┘└┘└─┘  ║ C|====|
 |    |  ╠════════════════════════════════════════════╣  |    |
 `----'  ║  Coffee smells like freshly ground heaven. ║  `----' 
         ╚════════════════════════════════════════════╝        
"""
    print(logo)

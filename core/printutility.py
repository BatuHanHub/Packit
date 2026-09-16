#region Texts
__version__ = "3.5"

banner = r"""
____             _     _ _   
|  _ \ __ _  ____| | __(_) |_ 
| |_) / _` |/ __| |/ /| | __|
|  __/ (_| | (__|   < | | |_ 
|_|   \__,_|\___|_|\_\|_|\__|

Packit - Cross-Platform CLI Package Management Automation Tool version {v}
https://github.com/BatuHanHub/Packit/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should receive a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
""".format(v=__version__)
#endregion

import os

# for windows ANSI color support
if(os.name == 'nt'):
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # ENABLE_PROCESSED_OUTPUT | ENABLE_WRAP_AT_EOL_OUTPUT | ENABLE_VIRTUAL_TERMINAL_PROCESSING = 7
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception as e:
        print(f"[ERROR] {e}")

class Color:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def pError(msg: str):
    print(f"{Color.RED}{Color.BOLD}[ERROR]{Color.RESET} {Color.RED}{msg}{Color.RESET}")

def pWarn(msg: str):
    print(f"{Color.YELLOW}{Color.BOLD}[WARN]{Color.RESET} {Color.YELLOW}{msg}{Color.RESET}")

def pInfo(msg: str):
    print(f"{Color.CYAN}{Color.BOLD}[INFO]{Color.RESET} {msg}")

def pSuccess(msg: str):
    print(f"{Color.GREEN}{Color.BOLD}[OK]{Color.RESET} {msg}")

def pTest(msg: str):
    print(f"{Color.MAGENTA}{Color.BOLD}[TEST]{Color.RESET} {Color.MAGENTA}{msg}{Color.RESET}")

def pPackitStatus():
    print(banner)
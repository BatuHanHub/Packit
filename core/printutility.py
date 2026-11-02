import os

# for windows ANSI color support
if os.name == 'nt':
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

def print_error(msg: str):
    print(f"{Color.RED}{Color.BOLD}[ERROR]{Color.RESET} {Color.RED}{msg}{Color.RESET}")

def print_warn(msg: str):
    print(f"{Color.YELLOW}{Color.BOLD}[WARN]{Color.RESET} {Color.YELLOW}{msg}{Color.RESET}")

def print_info(msg: str):
    print(f"{Color.CYAN}{Color.BOLD}[INFO]{Color.RESET} {msg}")

def print_success(msg: str):
    print(f"{Color.GREEN}{Color.BOLD}[OK]{Color.RESET} {msg}")

def print_test(msg: str):
    print(f"{Color.MAGENTA}{Color.BOLD}[TEST]{Color.RESET} {Color.MAGENTA}{msg}{Color.RESET}")
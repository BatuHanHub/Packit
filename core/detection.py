import os
from core.printutility import *

def get_current_os_base():
    if os.name in ["nt", "posix"]:
        return os.name
    return "unknown"

def check_platform_compatibility(json_data, test):
    target_os = json_data.get("system_info", {}).get("target_os_base", "unknown")
    current_os = get_current_os_base()

    if target_os == "unknown" or current_os == "unknown":
        print_warn(f"System base is set to 'unknown'. Proceeding anyway...")
        return True

    if target_os != current_os and not test:
        print_error(f"Platform mismatch! Target OS: '{target_os}', Current OS: '{current_os}'")
        return False

    elif target_os != current_os and test:
        print_warn(f"Platform mismatch! Target OS: '{target_os}', Current OS: '{current_os}'")
        return False

    print_success("Platform compatibility verified.")
    return True 
import os
import json
import shutil

def getSystemOSBase():
    if os.name in ["nt", "posix"]:
        return os.name
    return "unknown"

def checkPlatformCompatibility(jsonData):
    targetOS = jsonData.get("system_info", {}).get("target_os_base", "unknown")
    currectOS = getSystemOSBase()

    if(targetOS == "unknown" or currectOS == "unknown"):
        return True, f"[WARNING] System base is set to 'unknown'. Proceeding anyway..."

    if(targetOS != currectOS):
        return False, f"[ERROR] Platform mismatch! Target OS: '{targetOS}', Current OS: '{currectOS}'"

    return True, "[OK] Platform compatibility verified."
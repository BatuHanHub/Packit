import os
from core.printutility import *

def getSystemOSBase():
    if os.name in ["nt", "posix"]:
        return os.name
    return "unknown"

def checkPlatformCompatibility(jsonData, test):
    targetOS = jsonData.get("system_info", {}).get("target_os_base", "unknown")
    currentOS = getSystemOSBase()

    if(targetOS == "unknown" or currentOS == "unknown"):
        pWarn(f"System base is set to 'unknown'. Proceeding anyway...")
        return True

    if(targetOS != currentOS and not test):
        pError(f"Platform mismatch! Target OS: '{targetOS}', Current OS: '{currentOS}'")
        return False

    elif(targetOS != currentOS and test):
        pWarn(f"Platform mismatch! Target OS: '{targetOS}', Current OS: '{currentOS}'")
        return False

    pSuccess("Platform compatibility verified.")
    return True 
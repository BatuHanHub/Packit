import subprocess
from core.printutility import *

# Execute Script
def executeScript(scriptsDict, preScript, test=False):
    key = "pre_script" if preScript == 1 else "post_script"
    commands = scriptsDict.get(key, [])

    for cmd in commands:
        if(test):
            pTest(f"{cmd}")
        else:
            subprocess.run(cmd, shell=True)

# Update system
def executeUpdate(systemInfo, test=False):
    for key, value in systemInfo.items():
        if(isinstance(value, dict) and value.get("update")):
            cmd = value.get("update")

            if(test):
                pTest(f"{cmd}")

            else:
                subprocess.run(f"{cmd}", shell=True)

# Install packages
def executeInstall(systemInfo, packageMap, test=False):
    for key, pkgs in packageMap.items():
        if(not pkgs or key == "ignore"): # do not look ignore key datas
            continue

        managerKey = f"{key}_manager" # get keys for example: system_manaager, aur_manager, flatpak_manager ...
        manager = systemInfo.get(managerKey) # get package manager

        if(isinstance(manager, dict) and manager.get("install")):
            installCmd = manager["install"] 
            fullCmd = f"{installCmd} {' '.join(pkgs)}" # package_manager and packages

            if(test):
                pTest(f"{fullCmd}")

            else:
                subprocess.run(fullCmd, shell=True, check=True)

        else:
            if(test):
                pTest(f"No install command defined for '{key}' packages.(skipped)")

# Start execution
def startExecution(packageListPath, test=False):
    # get datas from json
    systemInfo = packageListPath.get("system_info", {})
    packages = packageListPath.get("packages", {})
    scripts = packageListPath.get("scripts", {})
    

    executeScript(scripts, 1, test) # pre script
    executeUpdate(systemInfo, test) # update
    executeInstall(systemInfo, packages, test) # install packages
    executeScript(scripts, 0, test) # last scripts
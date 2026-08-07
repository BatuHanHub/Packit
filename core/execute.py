import json
import subprocess
from core.resolver import resolvePackages

def executeScript(scriptsDict, preScript, test=False):
    if(preScript == 1):
        key = "pre_script"

    else: 
        key = "post_script"
    
    commands = scriptsDict.get(key, [])

    for cmd in commands:
        if (test):
            print(f"[TEST] {cmd}")
        else:
            subprocess.run(cmd, shell=True)

# Update system
def executeUpdate(updateCmd, test=False):
    for cmd in updateCmd:
        command = cmd["update"]

        for flag in cmd.get("flags", []): # split flags
            if(flag not in command):
                command += f" {flag}"

        if (test):
            print(f"[TEST] {cmd['update']}")

        else:
            subprocess.run(f"{cmd['update']}", shell=True)

# Install packages
def executeInstall(managers, packageMap, test=False):
    for manager in managers:
        packages = resolvePackages(manager, packageMap)

        if not packages:
            continue

        command = manager["install"]

        if (manager["flags"]):
            command += " " + " ".join(manager["flags"])

        command += " " + " ".join(packages)

        if (test):
            print(f"[TEST] {command}")

        else:
            subprocess.run(command, shell=True, check=True)

# Start execution
def startExecution(opSys, packageListPath, test=False):
    executeScript(packageListPath["scripts"], 1, test)
    executeUpdate(opSys, test)
    executeInstall(opSys, packageListPath["packages"], test)
    executeScript(packageListPath["scripts"], 0, test)
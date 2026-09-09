import subprocess

# Execute Script
def executeScript(scriptsDict, preScript, test=False):
    key = "pre_script" if preScript == 1 else "post_script"
    commands = scriptsDict.get(key, [])

    for cmd in commands:
        if(test):
            print(f"[TEST] {cmd}")
        else:
            subprocess.run(cmd, shell=True)

# Update system
def executeUpdate(systemInfo, test=False):
    for key, value in systemInfo.items():
        if(isinstance(value, dict) and value.get("update")):
            cmd = value.get("update")

            if(test):
                print(f"[TEST] {cmd}")

            else:
                subprocess.run(f"{cmd}", shell=True)

# Install packages
def executeInstall(systemInfo, packageMap, test=False):
    for key, pkgs in packageMap.items():
        if(not pkgs or key == "ignore"):
            continue

        managerKey = f"{key}_manager"
        manager = systemInfo.get(managerKey)

        if(isinstance(manager, dict) and manager.get("install")):
            installCmd = manager["install"]
            fullCmd = f"{installCmd} {' ' .join(pkgs)}"

            if(test):
                print(f"[TEST] {fullCmd}")

            else:
                subprocess.run(fullCmd, shell=True, check=True)

        else:
            if(test):
                print(f"[TEST SKIP] No install command defined for '{key}' packages.")

# Start execution
def startExecution(packageListPath, test=False):
    systemInfo = packageListPath.get("system_info", {})
    packages = packageListPath.get("packages", {})
    scripts = packageListPath.get("scripts", {})
    

    executeScript(scripts, 1, test)
    executeUpdate(systemInfo, test)
    executeInstall(systemInfo, packages, test)
    executeScript(scripts, 0, test)
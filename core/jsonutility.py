import json

def loadJson(file):
    try:
        with open(file, "r", encoding="utf8") as f:
            return json.load(f)
 
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file}")
        return None
 
    except json.JSONDecodeError as e:
        print(f"[ERROR] {file} is not valid JSON: {e}")
        return None

def generateJson(oprSysData, fileName):
    if (not fileName or isinstance(fileName, bool)):
        fileName = "template.json"

    if (not fileName.endswith(".json")):
        fileName += ".json"

    # operating system stuffs
    managers = []
    if (isinstance(oprSysData, list)):
        managers = oprSysData

    elif (isinstance(oprSysData, dict)):
        for key, val in oprSysData.items():
            if (isinstance(val, list)):
                managers.extend(val)

            elif (isinstance(val, dict)):
                managers.append(val)

    # Collect handles's 2th tag
    handles = set()
    for manager in managers:
        if isinstance(manager, dict):
            for handle in manager.get("handles", []):
                handles.add(handle)

    # adding packages subkeys
    packagesDict = {handle: [] for handle in sorted(handles)}
    packagesDict["ignore"] = []

    targetOS = "Unknown"
    targetBase = "Unknown"

    if (managers and isinstance(managers[0], dict)):
        targetOS = managers[0].get("os", "Unknown")
        targetBase = managers[0].get("base", "Unknown")

    config = {
        "meta": {
            "name": fileName[:-5],
            "version": "1.0.0",
            "description": ""
        },
        "system_info": {
            "target_os": targetOS,
            "target_base": targetBase,
        },
        "packages": packagesDict,
        "scripts": {
            "pre_script": [],
            "post_script": []
        }
    }

    try:
        with open(fileName, "w", encoding="utf8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        print(f"[OK] {fileName} created successfully")

    except OSError as e:
        print(f"[ERROR] Could not write {fileName}: {e}")

    return config
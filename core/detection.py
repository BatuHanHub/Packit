import json
import shutil

def init():
    packageManagers = []

    try:
        with open("./core/list.json", "r", encoding="utf8") as lst:
            listOfPackageManagers = json.load(lst)

            for osName, osPackageManagers in listOfPackageManagers.items():
                for pInfo in osPackageManagers:
                    packMngrName = pInfo.get("package_manager") or pInfo.get("pm")
                    
                    if packMngrName and shutil.which(packMngrName):
                        item = {"os": osName, **pInfo} 
                        packageManagers.append(item)

        if (not packageManagers):
            return "Unknown"

    except FileNotFoundError:
        return "[ERROR] list.json file not found. Please ensure the file exists in the correct directory."
    
    else:
        return packageManagers
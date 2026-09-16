import os
import json
import random
from core.printutility import *

EXAMPLES = [
    "Peace at home, peace in the world. -Mustafa Kemal Atatürk",
    "Victory is for those who can say “Victory is mine”. Success is for those who can begin saying “I will succeed.” and say “I have succeeded.” in the end. -Mustafa Kemal Atatürk",
    "Where there is no freedom, there is death and destruction. -Mustafa Kemal Atatürk",
    "The biggest war is the war against ignorance. -Mustafa Kemal Atatürk",
    "The most genuine guide in life is science. -Mustafa Kemal Atatürk",
    "They must all understand that we mean full independency when we say we want peace. -Mustafa Kemal Atatürk",
    "Freedom and independence form my character. -Mustafa Kemal Atatürk",

    "Let us love, let us be loved; the world shall be left to no one. -Yunus Emre",

    "Why should we build our happiness on the opinions of others, when we can find it in our own hearts? -J.J. Rousseau",

    "If fighting is sure to result in victory, then you must fight! Sun Tzu said that. -Soilder Boi&Sun Tzu",
    "Half Life 2 Episode 2, Team Fortress 2 and Portal... Three great games one orange box. Coming in october. -Lord GabeN",
    "This is gonna be a real piece of piss ya bloody fruit shop owners!",
    "Rise and shine, Mr. Freeman. Rise and... shine.",
    "Bingo, bango, bongo; bish, bash, bosh.",
    "The cake is a lie.",

    "War... War never changes.",
    "Press F to pay respects.",
    "Wake up, Samurai. We have a city to burn. -Johnny Silverhand",

    "I'm gonna make him an offer he can't refuse. -Vito Corleone",
    "There is no spoon."
]

def loadJson(file):
    try:
        with open(file, "r", encoding="utf8") as f:
            return json.load(f)
 
    except FileNotFoundError:
        pError(f"File not found: {file}")
        return None
 
    except json.JSONDecodeError as e:
        pError(f"{file} is not valid JSON: {e}")
        return None

def generateJson(targetOSBase, fileName):
    if (not fileName or isinstance(fileName, bool)):
        fileName = "template.json"

    if (not fileName.endswith(".json")):
        fileName += ".json"

    # json name
    nameOfJson = os.path.splitext(os.path.basename(fileName))[0] 

    # Linux/macos/BSD etc.
    #region posixJson
    if(targetOSBase == "posix"): 
        system_info = {
            "target_os_base": "posix",
            "system_manager": {
                "update": "",
                "install": ""
            },
            "aur_manager": {
                "update": "",
                "install": ""
            },
            "flatpak_manager": {
                "update": "flatpak update -y",
                "install": "flatpak install -y"
            }
        }
        packagesDict = {
            "system": [],
            "aur": [],
            "flatpak": [],
            "ignore": []
        }
    #endregion

    # region windowsJson
    elif(targetOSBase == "nt"): # windows
        system_info = {
            "target_os_base": "nt",
            "system_manager": {
                "update": "winget upgrade --all --accept-source-agreements --accept-package-agreements --silent",
                "install": "winget install --accept-source-agreements --accept-package-agreements --silent -e --id"
            }
        }
        packagesDict = {
            "system": [],
            "ignore": []
        }
    #endregion

    # region unknownJson
    else:
        system_info = {
            "target_os_base": "unknown",
            "system_manager": {
                "update": "",
                "install": ""
            }
        }
        packagesDict = {
            "system": [],
            "ignore": []
        }
    #endregion

    #region headJson
    config = {
        "meta": {
            "name": nameOfJson,
            "version": "1.0.0",
            "description": random.choice(EXAMPLES)
        },
        "system_info": system_info,
        "packages": packagesDict,
        "scripts": {
            "pre_script": [],
            "post_script": []
        }
    }
    #endregion

    try:
        # Create directory if not exists
        os.makedirs(os.path.dirname(fileName), exist_ok=True) if os.path.dirname(fileName) else None

        with open(fileName, "w", encoding="utf8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

        pInfo(f"{fileName} created successfully")

    except OSError as e:
        pError(f"Could not write {fileName}: {e}")

    return config
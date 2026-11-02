import os
import json
import random
from core.printutility import *
from core.examples import EXAMPLES

def load_json(file):
    try:
        with open(file, "r", encoding="utf8") as f:
            return json.load(f)
 
    except FileNotFoundError:
        print_error(f"File not found: {file}")
        return None
 
    except json.JSONDecodeError as e:
        print_error(f"{file} is not valid JSON: {e}")
        return None

def generate_json(target_os_base, filename):
    if not filename or isinstance(filename, bool):
        filename = "template.json"

    if not filename.endswith(".json"):
        filename += ".json"

    # json name
    json_name = os.path.splitext(os.path.basename(filename))[0] 

    
    #region posix_json
    if target_os_base == "posix": # Linux/macos/BSD etc.
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
        packages_dict = {
            "system": [],
            "aur": [],
            "flatpak": [],
            "ignore": []
        }
    #endregion

    # region windows_json
    elif target_os_base == "nt": # windows
        system_info = {
            "target_os_base": "nt",
            "system_manager": {
                "update": "winget upgrade --all --accept-source-agreements --accept-package-agreements --silent",
                "install": "winget install --accept-source-agreements --accept-package-agreements --silent -e --id"
            }
        }
        packages_dict = {
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
        packages_dict = {
            "system": [],
            "ignore": []
        }
    #endregion

    #region headJson
    config = {
        "meta": {
            "name": json_name,
            "version": "1.0.0",
            "description": random.choice(EXAMPLES)
        },
        "system_info": system_info,
        "packages": packages_dict,
        "scripts": {
            "pre_script": [],
            "mid_script": [],
            "post_script": []
        }
    }
    #endregion

    try:
        # Create directory if not exists
        os.makedirs(os.path.dirname(filename), exist_ok=True) if os.path.dirname(filename) else None

        with open(filename, "w", encoding="utf8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

        print_info(f"{filename} created successfully")

    except OSError as e:
        print_error(f"Could not write {filename}: {e}")

    return config
import sys
import json
import argparse
import subprocess

def generateJson(filePath):
    structure = {
        "sys": {
            "install": "",
            "update": ""
        },

        "pkgs": {
            "package": [],
            "flatpak": [],
            "shell": [],
            "ignore": []
        }
    }

    if(not filePath.endswith(".json")):
        filePath += ".json"

    with open(filePath, 'w') as f:
        json.dump(structure, f, indent=4)
    
    print(f"[Info] {filePath} file has been generated.")

def loadJson(filePath):
    try:
        with open(filePath, 'r') as f:
            return json.load(f)
        
    except FileNotFoundError:
        sys.exit(f"[Error] {filePath} file not found.")

    except json.JSONDecodeError:
        sys.exit(f"[Error] {filePath} could not be read.")


def execute(cmd, prt=True, pkgs='', merge=1):
    if (isinstance(pkgs, list) and merge == 1):
        cmdList = [f"{cmd} {' '.join(pkgs)}"]

    elif (isinstance(pkgs, list) and merge == 0):
        cmdList = [f"{cmd} {p}".strip() for p in pkgs]

    else:
        cmdList = [f"{cmd} {pkgs}".strip()]

    for cmd in cmdList:
        if (prt):
            print(f"[Info] >>> {cmd}\n")

        else:
            try:
                subprocess.run(cmd, check=True, shell=True)

            except subprocess.CalledProcessError as e:
                sys.exit(f"[Error] {e}")

def start(jsonFile, prt):
    print(f"[Info] {jsonFile} file is being read...")
    datas = loadJson(jsonFile)

    # System Update
    execute(datas['sys']['update'], prt)

    # Install all packages
    for pkg in datas['pkgs'].get('package', []):
        execute(datas['sys']['install'], prt, pkg)

    # Run shell commands
    execute("", prt, datas['pkgs'].get('shell', []), 0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file',
        type=str,
        help='JSON file path for installation'
    )
    parser.add_argument(
        '-t',
        '--test', 
        action='store_true',
        help='Show commands without executing them'
    )
    parser.add_argument(
        '-g',
        '--generate',
        nargs='?',
        const='template',
        metavar='FILE',
        help='Generate a JSON file (default: template.json)'
    )

    args = parser.parse_args()
    
    if (args.file):
        start(args.file, args.test)
        return

    elif (args.generate):
        generateJson(args.generate)
        return

if __name__ == "__main__":
    main()
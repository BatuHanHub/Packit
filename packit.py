import argparse
from core.detection import init
from core.execute import startExecution
from core.jsonutility import loadJson, generateJson

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description="Packit - Cross-platform package management automation tool")
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
        const='template.json',
        metavar='FILE',
        help='Generate a JSON file (default: template.json)'
    )

    args = parser.parse_args()

    opSys = init()
    print(opSys)

    if(args.file):
        startExecution(opSys, loadJson(args.file), args.test)

    elif(args.generate):
        generateJson(opSys, args.generate)
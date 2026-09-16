r"""
____             _     _ _   
|  _ \ __ _  ____| | __(_) |_ 
| |_) / _` |/ __| |/ /| | __|
|  __/ (_| | (__|   < | | |_ 
|_|   \__,_|\___|_|\_\|_|\__|

Packit - Cross-Platform CLI Package Management Automation Tool
https://github.com/BatuHanHub/Packit/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should receive a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
from core.detection import checkPlatformCompatibility
from core.execute import startExecution
from core.jsonutility import loadJson, generateJson
from core.printutility import pError, pPackitStatus

if (__name__ == "__main__"):
    #region Arguments
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
    parser.add_argument(
        '-x',
        '--os-base',
        type=str,
        choices=['nt', 'posix'],
        default='unknown',
        help='Operating system base for JSON generation (nt: Windows; posix: Linux, MacOS, BSD...)'
    )

    args = parser.parse_args()
    #endregion

    # executing
    if(args.file):
        data = loadJson(args.file)
        if(data):
            isCompatible = checkPlatformCompatibility(data, args.test)

            if(not isCompatible and not args.test):
                pError("Execution stopped due to OS mismatch. Use -t / --test to preview commands anyway.")

            else:
                try:
                    startExecution(data, test=args.test)

                except KeyboardInterrupt as k:
                    print("Cya!")

    # generate json
    elif(args.generate is not None):
        generateJson(args.os_base, args.generate)

    # nothing
    else:
        pPackitStatus()
        parser.print_help()
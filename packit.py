r"""
____             _     _ _   
|  _ \ __ _  ____| | __(_) |_ 
| |_) / _` |/ __| |/ /| | __|
|  __/ (_| | (__|   < | | |_ 
|_|   \__,_|\___|_|\_\|_|\__|

Packit v4.0 - Cross-Platform CLI Package Management Automation Tool
https://github.com/BatuHanHub/Packit/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
BatuHanHub, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should receive a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

__version__ = "4.0"

import argparse
from core.detection import check_platform_compatibility
from core.execute import start_execution
from core.jsonutility import load_json, generate_json
from core.printutility import print_error

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
    if args.file:
        data = load_json(args.file)
        if data:
            is_compatible = check_platform_compatibility(data, args.test)

            if not is_compatible and not args.test:
                print_error("Execution stopped due to operating system mismatch. Use -t / --test to preview commands anyway.")

            else:
                try:
                    start_execution(data, test=args.test)

                except KeyboardInterrupt as k:
                    print("Cya!")

    # generate json
    elif args.generate is not None:
        generate_json(args.os_base, args.generate)

    # nothing
    else:
        parser.print_help()
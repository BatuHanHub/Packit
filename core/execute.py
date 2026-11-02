import subprocess
from core.printutility import *
import datetime

log_filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f"{log_filename}.log"

# Execute Script
def execute_script(scripts_dict, mode_script, test=False):
    if(mode_script == 0):
        key = "pre_script"

    elif(mode_script == 1):
        key = "mid_script"

    elif(mode_script == 2):
        key = "post_script"

    commands = scripts_dict.get(key, [])

    for cmd in commands:
        if(test):
            print_test(f"{cmd}")
        else:
            with open(f"{log_filename}", "a") as log_file:
                log_file.write(f"Executing script: {key}\n")
                log_file.flush()
                subprocess.run(cmd, shell=True, stdout=log_file, stderr=log_file, check=True)

# Update system
def execute_update(system_info, test=False):
    for key, value in system_info.items():
        if(isinstance(value, dict) and value.get("update")):
            cmd = value.get("update")

            if(test):
                print_test(f"{cmd}")

            else:
                with open(f"{log_filename}", "a") as log_file:
                    log_file.write(f"Updating {key}...\n")
                    log_file.flush()
                    subprocess.run(f"{cmd}", shell=True, stdout=log_file, stderr=log_file, check=True)

# Install packages
def execute_install(system_info, package_map, test=False):
    for key, pkgs in package_map.items():
        if(not pkgs or key == "ignore"): # do not look ignore key datas
            continue

        manager_key = f"{key}_manager" # get keys for example: system_manaager, aur_manager, flatpak_manager ...
        manager = system_info.get(manager_key) # get package manager

        if(isinstance(manager, dict) and manager.get("install")):
            command_install = manager["install"] 
            command_full = f"{command_install} {' '.join(pkgs)}" # package_manager and packages

            if(test):
                print_test(f"{command_full}")

            else:
                with open(f"{log_filename}", "a") as log_file:
                    log_file.write(f"Installing {key} packages...\n")
                    log_file.flush()
                    subprocess.run(command_full, shell=True, check=True, stdout=log_file, stderr=log_file)

        else:
            if(test):
                print_test(f"No install command defined for '{key}' packages.(skipped)")

# Start execution
def start_execution(package_list_path, test=False):
    if not test:
        print_info("Starting execution...")
        with open(f"{log_filename}", "a") as log_file:
            log_file.write(f"Execution started at {log_filename}\n")
            log_file.flush()
    
    # get datas from json
    system_info = package_list_path.get("system_info", {})
    packages = package_list_path.get("packages", {})
    scripts = package_list_path.get("scripts", {})
    

    execute_script(scripts, 0, test) # pre script
    execute_update(system_info, test) # update
    execute_script(scripts, 1, test) # mid script(runs after update)
    execute_install(system_info, packages, test) # install packages
    execute_script(scripts, 2, test) # last scripts
# What is Packit?
Packit is a cross-platform package management automation tool. It installs packages defined in a JSON configuration file, making it easy to recreate your development environment on a new system.

# Features
- Cross-platform 
  - **Windows:** *winget*
  - **Linux:** *apt, rpm/dnf, pacman, paru/yay, flatpak...*
  - **MacOS:** *homebrew*
  - **BSD**
- JSON-based configuration
- Custom shell commands
- Dry-run mode
- Reusable configuration files

# JSON Configuration
```json
{
    /* it is title for your json file */
    "meta": { 
        "name": "template",
        "version": "1.0.0",
        "description": ""
    },
    /* this place define your operating system and distro for Linux users */
    "system_info": { 
        "target_os": "Linux",
        "target_base": "Arch"
    },
    /* your packages */
    "packages": {
        "aur": [
          "godot"
        ],
        "flatpak": [
          "org.blender.Blender"
        ],
        "system": [
          "blender",
          "firefox"
        ],
        "ignore": [
          "- ignore this packages -",
          "unityhub"
        ]
    },
    /* you can write bash/zsh/fish/powershell... scripts in here */
    "scripts": {
        "pre_script": [ // run before process
          "clear",
          "echo \"Starting...\""
        ],
        "post_script": [ // run after process
          "sudo reboot now"
        ]
    }
}
```

# Arguments
## Help
```bash
python packit.py -h
```
```bash
python packit.py --help
```

## Generate JSON file
```bash
python packit.py -g <file_name>
```
```bash
python packit.py --generate <file_name>
```
#### NOTE: If no file name is provided, template.json will be generated.

## Execute JSON file
```bash
python packit.py -f <file_name>
```
```bash
python packit.py --file <file_name>
```

## Testing
```bash
python packit.py -f <file_name> -t
```
```bash
python packit.py --file <file_name> --test
```

# Installation

```bash
git clone https://github.com/BatuHanHub/packit.git
cd Packit
python packit.py --help
```

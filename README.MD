# What is Packit?
Packit is a cross-platform package management automation tool. It installs packages defined in a JSON configuration file, making it easy to recreate your development environment on a new system.

# Features
- Cross-platform 
  - **Windows:** *winget*
  - **Linux:** *apt, rpm/dnf, pacman, paru/yay, flatpak*
  - **MacOS:** *homebrew*
  - **BSD**
- JSON-based configuration
- Custom shell commands
- Dry-run mode
- Reusable configuration files

# JSON Configuration
```json
{
  // commands used to install and update packages
  // replace them with the commands for your package manager
  "sys": {
    "install": "flatpak install -y",
    "update": "flatpak update -y"
  },

  "pkgs": {
    // package to install
    "package": [
      "org.mozilla.firefox"
      /* More Packages */
    ],
    // shell commands to execute after installation
    "shell": [
        "echo \"Finished -> Flatpak\"",
        "python3 packit.py -f my_setup.json" // you can execute another Packit configuration
    ],
    // packages or commands to ignore
    "ignore": [
      "xxx.ignore.yyy",
      "sudo rm -rf /"
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
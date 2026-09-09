# Packit 📦

**Packit** is a lightweight, cross-platform package management automation CLI tool. It installs packages and executes custom setup commands defined in declarative JSON configuration files, making it effortless to recreate your environment across different operating systems.

---

## Key Features

- **Cross-Platform Compatibility:** Works seamlessly on Linux, macOS, Windows, and BSD environments.
- **Declarative Configuration:** Driven entirely by explicit JSON files — no fragile dynamic system scanning.
- **Manager Agnostic:** Define any package manager you want (`pacman`, `paru`, `apt`, `winget`, `brew`, `flatpak`, `emerge`, etc.).
- **Pre & Post Execution Scripts:** Run custom shell/terminal commands before and after package installation.
- **Dry-Run Mode (`-t`):** Preview commands safely in the terminal without making system changes.
- **Auto Template Generator (`-g`):** Generate pre-configured OS templates on the fly.

---

## JSON Schema

The configuration file serves as the single source of truth for your system setup. 

```json
{
    "meta": {
        "name": "template linux json file",
        "version": "1.0.0",
        "description": "Victory is for those who can say “Victory is mine”. Success is for those who can begin saying “I will succeed.” and say “I have succeeded.” in the end. -Mustafa Kemal Atatürk"
    },
    "system_info": {
        "target_os_base": "posix",
        "system_manager": {
            "update": "sudo pacman -Syu --noconfirm",
            "install": "sudo pacman -S --noconfirm"
        },
        "aur_manager": {
            "update": "paru -Syu --noconfirm --sudoloop",
            "install": "paru -S --noconfirm --sudoloop"
        },
        "flatpak_manager": {
            "update": "flatpak update -y",
            "install": "flatpak install -y"
        }
    },
    "packages": {
        "system": [
            "blender",
            "firefox"
        ],
        "aur": [
            "godot"
        ],
        "flatpak": [
            "org.blender.Blender"
        ],
        "ignore": [
            "unityhub"
        ]
    },
    "scripts": {
        "pre_script": [
            "clear",
            "echo \"Starting setup...\""
        ],
        "post_script": [
            "echo \"Installation completed successfully!\""
        ]
    }
}

```

> **How Execution Works:**
> Packit matches package array keys (e.g., `"aur"`) to their corresponding manager command in `system_info` (e.g., `"aur_manager"`). Any undefined manager or empty package array will be skipped gracefully without breaking execution.

---

## Usage & Arguments

### 1. View Help 📖

```bash
python packit.py -h

```

### 2. Generate Template JSON 📄

Generate a starter configuration file based on your OS platform base (`posix` or `nt`):

```bash
# Generate default template.json
python packit.py -g

# Generate for Linux / macOS / BSD
python packit.py -g myconfig.json -x posix

# Generate for Windows
python packit.py -g myconfig.json -x nt

```

### 3. Test Run (Dry-Run Mode) 🧪

Preview all commands in sequence without executing them on your system:

```bash
python packit.py -f ./jsons/linux/archlinux.json -t
```

### 4. Execute Installation 🚀

Run package updates, install packages, and execute scripts:

```bash
python packit.py -f ./jsons/linux/archlinux.json
```

---

## Quick Start 🏃

```bash
# Clone the repository
git clone https://github.com/BatuHanHub/Packit.git
cd Packit

# Generate a starter configuration
python packit.py -g home-setup.json -x posix
python packit.py -g work-setup.json -x posix

# Preview the commands
python packit.py -f home-setup.json -t
python packit.py -f work-setup.json -t
```
> **Note:**
> Depending on your operating system or Linux distribution, the Python executable might be named `python3` instead of `python`. If the command fails, try running `python3 packit.py ...`.
---
# Raspkei for the Raspberry Pi
![GITHUB](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![RELEASE](https://img.shields.io/github/v/release/KeiBlackley/Raspkei.svg) ![LICENCE](https://img.shields.io/github/license/KeiBlackley/Raspkei.svg) ![ISSUES](https://img.shields.io/github/issues/KeiBlackley/Raspkei.svg)

Raspberry Pi scripting tool for automation, designed to simplify tasks and improve efficiency.

## Table of Contents
- [About](#about)
    * [What's New](#whats-new)
    * [Screenshots](#screenshots)
    * [Features](#features)
- [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Testing](#testing)
    * [Execute](#execute) 
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Usage](#usage)
- [Licence](#license)
- [About the Developer](#about-the-developer)
- [Credits & Acknowledgements](#credits--acknowledgements)
<hr/>

### About
Essentially Raspkei is a set of scripts setup to help users configure and use their Raspberry Pi device.

Mainly coded in Python3, also using shell, batch (for external Windows) and specific made programs to help automate and assist the user experience.

This project is open-source as long as credentials of Original Developer ("@KeiBlackley"/GitHub) are mentioned and licence is copied over.

*Not all elements of Raspkei may be in this Documentation. Feel free to use this file as a guide.*

<hr/>

### Getting Started
#### Prerequisites
None should be needed if setup scripts are run correctly.
Otherwise here they are:
- PHP8
- MariaDB
- Apache2
- git

#### Installation
> Clone repository
```bash
git clone https://github.com/KeiBlackley/Raspkei
```

> Set permissions
```bash
cd Raspkei

sudo chmod +x install.sh
```

> Run installation
```bash
./install.sh
```

> You should see a message like:
```bash
[2025-08-18 07:27:00] [INFO] Raspkei Installation Complete.
```

### Testing
> Set permissions
```
cd Raspkei

sudo chmod +x test.sh
```

> Run test script
```bash
./test.sh
```

### Execute
If `run.sh` exists:
> Set permissions
```bash
cd Raspkei

sudo chmod +x run.sh
```

> Run Raspkei
```bash
./run.sh
```

If `raspkei.py` exists and Python installed:
> Run Raspkei
```bash
cd Raspkei

python raspkei.py
python3 raspkei.py 		# use for Python3
```

### Quick Start
```
usage: raspkei [options] app_name run_boolean
  options:
    -u required_string			Sets SSID of Hotspot
    -p required_string     		Sets Password of Hotspot
    -n, --portal required_boolean     	Toggles Captive Portal
```

### Project Structure
```
├── app/
│   ├── raspkei.py         	# Application (python)
│   └── run.sh			# Application (shell)
├── assets/
├── └── css/
├── └── images/			# Assets Folder
├── └── scripts/
├── backups/
│   ├── images/			# Image Backups of Raspberry Pi OS
└── index.html            	# Web Docs
└── README.md            	# Documentation (this file)
```

### Technical Details
This project uses the following resources:

- **Hotspot:** [RaspAP](https://raspap.com/) and [nodogsplash](https://nodogsplash.readthedocs.io/en/latest/)
	- *Optional:* VPN Provider (w/ OpenVPN)
	- *Optional:* ADGuard DNS/Setup
- **Web Assets:** keiom.com

### Usage
- **Hotspot:**
> SSID: Raspkei Hotspot
PWD: sayplease
	- **Captive Portal:** [raspkei.local:2050](http://raspkei.local:2050)
		- **Gateway:** [raspkei.local](http://raspkei.local)
	

<hr/>

### Support
> Show your support with a donation to the project.

[![PAYPAL](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/KeiBlackley)










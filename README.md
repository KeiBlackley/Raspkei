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

This project is *Open-Source* **as long as** *credentials of the Original Developer* ("[@KeiBlackley](https://github.com/KeiBlackley)"/GitHub) or ("[Keirran Blaclkey](https://keirranblackley.com)") *are mentioned* and **Licence** is *copied over*.

**Not all elements of Raspkei may be in this Documentation. Feel free to use this file as a guide rather than instructions. Thank you**

<hr/>

### Getting Started
### Prerequisites
#### Hardware
<details>
<summary> Raspberry Pi </summary>
A single <a href="https://www.raspberrypi.org/computers">Raspberry device</a> is required for this, the 3B+ is recommended for it's wireless options and portbut the complete project is being tested on:

- 3 x RPi 3B+ (raspkei, raspkei3, raspkei3bp)
- 1 x RPi 3B (raspkei3b)
</details>
<details>
<summary> Accessories </summary>
For The Raspkei Hotspot to work as a Wireless Access Point, you can use an Ethernet cable to be the Internet Input, otherwise for portability a USB Modem can be used. 

The one being used and tested for this project is:

- <a href="https://www.telstra.com.au/internet/mobile-broadband/prepaid/4gx-mf833v-usb" target="_blank">Telstra 4G MF833v Modem</a>

For additional portability, a battery powered UPS is used:

- <a href="https://www.amazon.com.au/dp/B08BRPLY15" taget="_blank">Waveshare UPS HAT</a>
</details>

#### Software
<details>
<summary> Pre-Boot </summary>
- <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a> [SSH Enabled / Hostname: <code>raspkei</code>]
</details>
<details>
<summary> Dependencies </summary>
If setup scripts are not run correctly, install the following:

- Webserver:
    - PHP8
    - MariaDB
    - Apache2
    - git

- Hotspot:
    - hostapd
    - dnsmasq
    - iptables
</details>

#### Installation
> Clone repository
```bash
git clone https://github.com/KeiBlackley/Raspkei
```

> Set executes permissions
```bash
cd Raspkei

sudo chmod +x run.sh
```

> Run start script
```bash
./run.sh
```

### Testing
> Hotspot connection
```
SSID: Raspkei
PSW: [ check file / customise ]

./run.sh hotspot
./run.sh checkhotspot
```

> You should see messages like:
```
running, correct, enabled, complete
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
./run.sh [command]
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
usage: raspkei [options]
  options:
    --apache required_boolean [on/off]			Installs Apache Web Server
    --hotspot required_boolean [on/off]         Sets up WiFi Access Point
```

### Project Structure
```
Raspkei
    -> web      # Web Server Files
        -> runapache, resetapache
    -> wifi     # Hotspot Files
        -> runhotspot
    -> win      # Windows Files 
```

### Technical Details
This project uses the following resources:

- **Web Server:** [Apache](https://www.apache.org/)
    - [MariaDB](https://mariadb.org/)
    - [PHP](https://www.php.net/)
- **Hotspot:** [RaspAP](https://raspap.com/) and *Optional:*[nodogsplash](https://nodogsplash.readthedocs.io/en/latest/)
	- *Optional:* VPN Provider (w/ OpenVPN)
	- *Optional:* ADGuard DNS/Setup

### Usage
> Hotspot

SSID: Raspkei Hotspot
PWD: sayplease
	- **Captive Portal:** [raspkei.local:2050](http://raspkei.local:2050)
		- **Gateway:** [raspkei.local](http://raspkei.local)
	

<hr/>

### Support
> Show your support with a donation to the project.

[![PAYPAL](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/KeiBlackley)










#!/usr/bin/env python3
# Raspkei Hotspot Setup Script
# Sets up a WiFi hotspot (SSID: Raspkei, Password: sayplease) on wlan0, shares internet from usb0, and enables auto-run on boot.
import os
import subprocess
import sys

SSID = "Raspkei"
PASSWORD = "FuckOff123"
AP_INTERFACE = "wlan0"
INET_INTERFACE = "usb0"

def run(cmd, check=True):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        sys.exit(result.returncode)
    return result

def install_packages():
    pkgs = ["hostapd", "dnsmasq", "iptables"]
    missing = [pkg for pkg in pkgs if subprocess.run(f"dpkg -s {pkg}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0]
    if missing:
        run("sudo apt-get update")
        run(f"sudo apt-get install -y {' '.join(missing)}")
    run("sudo systemctl unmask hostapd")
    run("sudo systemctl enable hostapd")

def configure_hostapd():
    conf = f"""
interface={AP_INTERFACE}
driver=nl80211
ssid={SSID}
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase={PASSWORD}
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
"""
    with open("/etc/hostapd/hostapd.conf", "w") as f:
        f.write(conf)
    # Set DAEMON_CONF in /etc/default/hostapd
    run('sudo sed -i "s|^#DAEMON_CONF=.*|DAEMON_CONF=\"/etc/hostapd/hostapd.conf\"|g" /etc/default/hostapd')

def configure_dnsmasq():
    if os.path.exists("/etc/dnsmasq.conf"):
        run("sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig", check=False)
    conf = f"""
interface={AP_INTERFACE}
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
"""
    with open("/etc/dnsmasq.conf", "w") as f:
        f.write(conf)

def configure_network():
    run(f"sudo ip link set {AP_INTERFACE} down")
    result = subprocess.run(f"ip addr show {AP_INTERFACE}", shell=True, capture_output=True, text=True)
    if "192.168.4.1/24" not in result.stdout:
        run(f"sudo ip addr add 192.168.4.1/24 dev {AP_INTERFACE}")
    else:
        print(f"IP 192.168.4.1/24 already assigned to {AP_INTERFACE}")
    run(f"sudo ip link set {AP_INTERFACE} up")

def enable_ip_forwarding():
    run("sudo sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf", check=False)
    run("sudo sh -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'", check=False)

def configure_nat():
    run(f"sudo iptables -t nat -C POSTROUTING -o {INET_INTERFACE} -j MASQUERADE", check=False)
    run(f"sudo iptables -t nat -A POSTROUTING -o {INET_INTERFACE} -j MASQUERADE", check=False)
    run("sudo sh -c 'iptables-save > /etc/iptables.ipv4.nat'", check=False)
    rc_local = "/etc/rc.local"
    if not os.path.exists(rc_local):
        rc_local_content = """#!/bin/sh -e
# rc.local
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will 'exit 0' on success or any other value on error.
# By default this script does nothing.

exit 0
"""
        with open(rc_local, "w") as f:
            f.write(rc_local_content)
        os.chmod(rc_local, 0o755)
    with open(rc_local, "r") as f:
        lines = f.readlines()
    if "iptables-restore < /etc/iptables.ipv4.nat" not in ''.join(lines):
        for i, line in enumerate(lines):
            if line.strip() == "exit 0":
                lines.insert(i, "iptables-restore < /etc/iptables.ipv4.nat\n")
                break
        with open(rc_local, "w") as f:
            f.writelines(lines)

def enable_services():
    # Stop services first for a clean restart
    run("sudo systemctl stop hostapd", check=False)
    run("sudo systemctl stop dnsmasq", check=False)
    run("sudo systemctl start hostapd", check=False)
    run("sudo systemctl start dnsmasq", check=False)

def setup_systemd_service():
    service_content = f"""
[Unit]
Description=Raspkei Hotspot Setup
After=network.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 {os.path.abspath(__file__)}
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
"""
    service_path = "/etc/systemd/system/raspkei-hotspot.service"
    with open(service_path, "w") as f:
        f.write(service_content)
    run("sudo systemctl enable raspkei-hotspot.service", check=False)

def main():
    install_packages()
    configure_hostapd()
    configure_dnsmasq()
    configure_network()
    enable_ip_forwarding()
    configure_nat()
    enable_services()
    setup_systemd_service()
    print("Hotspot setup complete. Reboot to activate.")

# Device mapping file template for PHP integration
DEVICE_MAP_PATH = "/etc/raspkei_devices.txt"
if not os.path.exists(DEVICE_MAP_PATH):
    with open(DEVICE_MAP_PATH, "w") as f:
        f.write("# MAC_ADDRESS Device_Name\n")
        f.write("b8:27:eb:12:34:56 Raspberry Pi\n")
        f.write("f4:5c:89:ab:cd:ef Android Tablet\n")
        f.write("# Add more MAC-to-name mappings here\n")

if __name__ == "__main__":
    main()

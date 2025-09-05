#!/usr/bin/env python3
# Raspkei Hotspot Diagnostic Script
# Checks if the hotspot is set up and running correctly.

import subprocess
import sys
import os

def check_service(service):
    result = subprocess.run(f"systemctl is-active {service}", shell=True, capture_output=True, text=True)
    return result.stdout.strip() == "active"

def check_hostapd_conf():
    conf_path = "/etc/hostapd/hostapd.conf"
    if not os.path.exists(conf_path):
        print(f"hostapd config not found: {conf_path}")
        return False
    with open(conf_path) as f:
        conf = f.read()
    if "ssid=Raspkei" in conf and "wpa_passphrase=sayplease" in conf:
        print("hostapd config looks correct.")
        return True
    print("hostapd config missing SSID or password.")
    return False

def check_dnsmasq_conf():
    conf_path = "/etc/dnsmasq.conf"
    if not os.path.exists(conf_path):
        print(f"dnsmasq config not found: {conf_path}")
        return False
    with open(conf_path) as f:
        conf = f.read()
    if "interface=wlan0" in conf and "dhcp-range=192.168.4.2,192.168.4.20" in conf:
        print("dnsmasq config looks correct.")
        return True
    print("dnsmasq config missing interface or DHCP range.")
    return False

def check_ip_forwarding():
    result = subprocess.run("sysctl net.ipv4.ip_forward", shell=True, capture_output=True, text=True)
    return "net.ipv4.ip_forward = 1" in result.stdout

def check_nat():
    result = subprocess.run("sudo iptables -t nat -S POSTROUTING", shell=True, capture_output=True, text=True)
    return "-A POSTROUTING -o usb0 -j MASQUERADE" in result.stdout

def check_wlan_ip():
    result = subprocess.run("ip addr show wlan0", shell=True, capture_output=True, text=True)
    return "192.168.4.1/24" in result.stdout

def main():
    print("Checking hostapd service...")
    if check_service("hostapd"):
        print("hostapd is running.")
    else:
        print("hostapd is NOT running.")
    print("Checking dnsmasq service...")
    if check_service("dnsmasq"):
        print("dnsmasq is running.")
    else:
        print("dnsmasq is NOT running.")
    print("Checking hostapd config...")
    check_hostapd_conf()
    print("Checking dnsmasq config...")
    check_dnsmasq_conf()
    print("Checking IP forwarding...")
    if check_ip_forwarding():
        print("IP forwarding is enabled.")
    else:
        print("IP forwarding is NOT enabled.")
    print("Checking NAT (iptables)...")
    if check_nat():
        print("NAT is set up for usb0.")
    else:
        print("NAT is NOT set up for usb0.")
    print("Checking wlan0 IP address...")
    if check_wlan_ip():
        print("wlan0 has correct IP address.")
    else:
        print("wlan0 does NOT have correct IP address.")
    print("Diagnostics complete.")

if __name__ == "__main__":
    main()

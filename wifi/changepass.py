#!/usr/bin/env python3
# Raspkei Hotspot Password Change Script
# Changes the WiFi hotspot password live and restarts hostapd.
import sys
import os
import subprocess

CONF_PATH = "/etc/hostapd/hostapd.conf"

if len(sys.argv) != 2:
    print("Usage: sudo python3 changepass.py <new_password>")
    sys.exit(1)

new_password = sys.argv[1]

if not os.path.exists(CONF_PATH):
    print(f"hostapd config not found: {CONF_PATH}")
    sys.exit(1)

with open(CONF_PATH, "r") as f:
    lines = f.readlines()

changed = False
for i, line in enumerate(lines):
    if line.startswith("wpa_passphrase="):
        lines[i] = f"wpa_passphrase={new_password}\n"
        changed = True
        break

if not changed:
    print("wpa_passphrase line not found in config.")
    sys.exit(1)

with open(CONF_PATH, "w") as f:
    f.writelines(lines)

print(f"Password changed to: {new_password}")
print("Restarting hostapd...")
subprocess.run("sudo systemctl restart hostapd", shell=True)
print("Done.")

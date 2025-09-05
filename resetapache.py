#!/usr/bin/python3

import subprocess
import os

APACHE_SERVICE = "apache2"
WEB_ROOT = "/var/www/html"

# Stop and remove Apache
print("==> Stopping and removing Apache.")
subprocess.run(["sudo", "systemctl", "stop", APACHE_SERVICE])
subprocess.run(["sudo", "apt-get", "remove", "--purge", "-y", APACHE_SERVICE])
subprocess.run(["sudo", "apt-get", "autoremove", "-y"])

# Remove PHP
print("==> Removing PHP.")
subprocess.run(["sudo", "apt-get", "remove", "--purge", "-y", "php", "php-mysql", "libapache2-mod-php"])
subprocess.run(["sudo", "apt-get", "autoremove", "-y"])

# Stop and remove MariaDB
print("==> Stopping and removing MariaDB.")
subprocess.run(["sudo", "systemctl", "stop", "mariadb"])
subprocess.run(["sudo", "apt-get", "remove", "--purge", "-y", "mariadb-server", "mariadb-client"])
subprocess.run(["sudo", "apt-get", "autoremove", "-y"])

# Remove web root files
print(f"==> Removing all files in {WEB_ROOT}.")
subprocess.run(["sudo", "rm", "-rf", os.path.join(WEB_ROOT, "*")])

print("=== Web server and dependencies have been reset and removed. ===")

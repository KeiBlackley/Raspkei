import os
import subprocess
import sys

APACHE_SERVICE = "apache2"
WEB_ROOT = "/var/www/html"
INDEX_HTML = os.path.join(WEB_ROOT, "index.html")

def secure_sql():
    subprocess.run(["sudo", "mysql_secure_installation"])
    subprocess.run(["sudo", "service", "apache2", "restart"])

def install_dependencies():
    print("Installing PHP...\n")
    subprocess.run(["sudo", "apt-get", "install", "-y", "php"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "php-mysql"])
    subprocess.run(["sudo", "apt", "install", "-y", "libapache2-mod-php"])

    print("Installing MariaDB...\n")
    subprocess.run(["sudo", "apt-get", "install", "-y", "mariadb-server", "mariadb-client"])
    secure_sql()

# Install Apache
def install_apache():
    print("Installing Apache...\n")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", APACHE_SERVICE])

def is_php_installed():
    result = subprocess.run(["which", "php"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def is_mariadb_installed():
    result = subprocess.run(["which", "mariadb"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

# Check if Apache is installed
def is_apache_installed():
    result = subprocess.run(["which", APACHE_SERVICE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def start_mariadb():
    print("Enabling MariaDB...\n")
    subprocess.run(["sudo", "systemctl", "start", "mariadb"])
    subprocess.run(["sudo", "systemctl", "enable", "mariadb"])
    print("Securing MariaDB...\n")
    subprocess.run(["sudo", "mariadb-secure-installation"])

# Start Apache service
def start_apache():
    print("Starting Apache service...\n")
    subprocess.run(["sudo", "systemctl", "start", APACHE_SERVICE])
    subprocess.run(["sudo", "systemctl", "enable", APACHE_SERVICE])

def is_raspberry_pi():
    # Check for Raspberry Pi by reading /proc/cpuinfo
    try:
        with open("/proc/cpuinfo", "r") as f:
            cpuinfo = f.read().lower()
        return "raspberry pi" in cpuinfo or "bcm" in cpuinfo
    except Exception:
        return False

if __name__ == "__main__":
    if not is_raspberry_pi():
        print("This script can only be run on a Raspberry Pi.")
        sys.exit(1)
    if not is_php_installed():
        install_php()
    if not is_mariadb_installed():
        install_mariadb()
    if not is_apache_installed():
        install_apache()
    else:
        print(f"Web server is already installed.\n")
    start_apache()
    # Print IP address from ifconfig
    try:
        result = subprocess.run(["ifconfig"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        import re
        # Find all IPv4 addresses except 127.0.0.1
        ips = re.findall(r'inet (?!127)([0-9]+(?:\.[0-9]+){3})', result.stdout)
        if ips:
            print(f"Setup complete. Visit http://{ips[0]} in your browser.")
        else:
            print("Setup complete. Could not determine IP address from ifconfig.")
    except Exception as e:
        print("Setup complete. Could not determine IP address from ifconfig.")

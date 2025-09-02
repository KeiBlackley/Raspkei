import subprocess
import sys
import os

def run(cmd, check=True):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        sys.exit(result.returncode)
    return result

def run_hotspot_script():
    hotspot_script = os.path.join(os.path.dirname(__file__), "runhotspot.py")
    if not os.path.exists(hotspot_script):
        print("Hotspot script not found!")
        sys.exit(1)
    run(f"sudo python3 {hotspot_script}")

def install_apache():
    # Check if apache2 is installed
    if subprocess.run("dpkg -s apache2", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
        run("sudo apt-get update")
        run("sudo apt-get install -y apache2")
    run("sudo systemctl enable apache2")
    run("sudo systemctl start apache2")
    print("Apache installed and started.")

def main():
    run_hotspot_script()
    install_apache()
    print("Hotspot and Apache setup complete.")

if __name__ == "__main__":
    main()
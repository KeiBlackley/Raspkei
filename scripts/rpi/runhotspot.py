import subprocess

SSID = "Raspkei"
PASSWORD = "sayplease"
ETH_IFACE = "usb0"
WIFI_IFACE = "wlan0"
HOTSPOT_IP = "192.168.50.1"
DHCP_RANGE = "192.168.50.10,192.168.50.100,12h"

def run(cmd):
    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def configure_network():
    # Assign static IP to WiFi interface
    run(["sudo", "ip", "addr", "add", f"{HOTSPOT_IP}/24", "dev", WIFI_IFACE])
    run(["sudo", "ip", "link", "set", WIFI_IFACE, "up"])

def enable_ip_forwarding():
    run(["sudo", "sysctl", "-w", "net.ipv4.ip_forward=1"])

def setup_iptables():
    run(["sudo", "iptables", "-t", "nat", "-A", "POSTROUTING", "-o", ETH_IFACE, "-j", "MASQUERADE"])
    run(["sudo", "iptables", "-A", "FORWARD", "-i", ETH_IFACE, "-o", WIFI_IFACE, "-m", "state", "--state", "RELATED,ESTABLISHED", "-j", "ACCEPT"])
    run(["sudo", "iptables", "-A", "FORWARD", "-i", WIFI_IFACE, "-o", ETH_IFACE, "-j", "ACCEPT"])

def write_hostapd_conf():
    conf = f"""interface={WIFI_IFACE}
driver=nl80211
ssid={SSID}
hw_mode=g
channel=6
wmm_enabled=1
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase={PASSWORD}
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
"""
    with open("/tmp/hostapd.conf", "w") as f:
        f.write(conf)

def write_dnsmasq_conf():
    conf = f"""interface={WIFI_IFACE}
dhcp-range={DHCP_RANGE}
address=/#/{HOTSPOT_IP}
"""
    with open("/tmp/dnsmasq.conf", "w") as f:
        f.write(conf)

def start_services():
    run(["sudo", "hostapd", "/tmp/hostapd.conf"])
    run(["sudo", "dnsmasq", "--conf-file=/tmp/dnsmasq.conf"])

def main():
    configure_network()
    enable_ip_forwarding()
    setup_iptables()
    write_hostapd_conf()
    write_dnsmasq_conf()
    start_services()
    print(f"Hotspot '{SSID}' started on {WIFI_IFACE} with uplink {ETH_IFACE}.")

if __name__ == "__main__":
    main()

# Create User
sudo adduser <name>

# Delete User
sudo deluser -r <name>

# Set Permissions
sudo usermod -G adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev <name>

# Install Apache (installs php, mariadb)
python scripts/pi/runapache.py

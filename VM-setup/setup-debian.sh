#!/bin/bash 

# Update system
apt update && apt upgrade -y 

# Install basic tools
apt install -y nano vim curl wget dnsutils 

# Tangentbord & timezone
loadkeys sv 
localectl set-keymap sv 
timedatectl set-timezone Europe/Stockholm
echo "==== Setup done! ===="

# Install SSH
apt install openssh-server -y 
systemctl enable ssh 
systemctl start ssh
echo "====SSH aktiv port 22===="

# Install Tailscale 
curl -fsSL https://tailscale.com/install.sh | sh
echo "====Run: tailscale up --ssh===="

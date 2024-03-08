#!/bin/bash

# Install Nginx
apt-get update
apt-get install -y nginx

# Check if Nginx is running and listening on port 80
if ss -tuln | grep -q ':80'; then
    echo "Nginx is already running and listening on port 80."
else
    # Configure Nginx to listen on port 80
    sed -i 's/listen 80 default_server;/listen 80;/g' /etc/nginx/sites-available/default

    # Restart Nginx
    systemctl restart nginx

    echo "Nginx has been configured to listen on port 80."
fi

#!/usr/bin/env bash
# This script configures Nginx to listen on port 80.

# Check if Nginx is installed
if ! command -v nginx &> /dev/null; then
    echo "Nginx is not installed. Installing it now..."
    apt-get update
    apt-get install -y nginx

    # Check if installation was successful
    if [ $? -ne 0 ]; then
        echo "Failed to install Nginx. Exiting."
        exit 1
    fi
fi

# Check if Nginx is running
if service nginx status | grep -q "inactive"; then
    echo "Starting Nginx..."
    service nginx start
fi

# Check if Nginx is listening on port 80
if ! netstat -tuln | grep -q ":80 "; then
    # Add configuration to listen on port 80
    echo "Configuring Nginx to listen on port 80..."
    echo "server {
        listen 80;
        server_name _;
        location / {
            root /usr/share/nginx/html;
            index index.html index.htm;
        }
    }" > /etc/nginx/sites-available/default

    # Reload Nginx to apply changes
    service nginx reload
fi

echo "Nginx is now configured to listen on port 80."

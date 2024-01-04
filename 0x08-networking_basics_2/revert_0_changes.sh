#!/bin/bash

# Check if the script is run with sudo
if [ "$EUID" -ne 0 ]; then
    echo "Please run the script with sudo: sudo $0"
    exit 1
fi

# Check if a backup file exists
if [ -f "/etc/hosts.bak" ]; then
    # Restore the original /etc/hosts file
    cp /etc/hosts.bak /etc/hosts
    rm /etc/hosts.bak

    # Display success message
    echo "Reverted changes successfully!"
else
    echo "Backup file not found. No changes to revert."
fi
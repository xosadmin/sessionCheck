#!/bin/bash

dstFolder="/opt/bgpmon"

if [[ ! -d "$dstFolder" ]]; then
    mkdir -p "$dstFolder"
fi

if [[ $(dpkg -l | grep -oc "python") -eq "0" ]]; then
    echo "Python is not installed." >&2
    exit 1
fi

echo "Installing dependencies..."
pip3 install -r requirements.txt --break-system-package

echo "Coping files..."
cp -r utils "$dstFolder"
cp -r *.py "$dstFolder"
cp -r example-config.yaml "${dstFolder}/config.yaml"

echo "Installing system service..."
cp -r axbgpmon.service "/etc/systemd/system"
systemctl daemon-reload
systemctl enable axbgpmon

echo "Completed. Go ahead to ${dstFolder}/config.yaml for final configurations."
echo "The service is enabled. To start the service now, use: systemctl start axbgpmon"
#!/bin/bash

echo "Hey user, insert the IP that you want me to scan: "
read ip

echo "How many seconds the socket is going to wait until timeout: "
read delay

if [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo -e "Waiting for the scan..."
    python3 main.py "$ip" "$delay"
else
    echo "It's not a valid IP. Try again..."
fi

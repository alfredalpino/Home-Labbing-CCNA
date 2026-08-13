#!/bin/bash

echo "===== SYSTEM INFO ====="

echo "User: $USER"
echo "Hostname: $(hostname)"
echo "Kernel: $(uname -r)"
echo "Uptime: $(uptime)"
echo "Disk:"
df -h

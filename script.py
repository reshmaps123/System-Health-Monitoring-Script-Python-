#!/usr/bin/env python3

import psutil
import logging

# Set up logging
logging.basicConfig(filename='/var/log/system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {usage}%')

def check_memory_usage():
    memory = psutil.virtual_memory()
    usage = memory.percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {usage}%')

def check_disk_usage():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        logging.warning(f'Low Disk space available: {usage}%')

def check_system_health():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()

if __name__ == "__main__":
    check_system_health()

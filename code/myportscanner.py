#!/usr/bin/env python3

import sys
import socket
from datetime import datetime

# Usage
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("syntax: python3 scanner.py <ip>")

# Banner
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

# Scan
try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"port {port} is open")
        else:
            print(f"port {port} not open")
    s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Couldnt connect to server.")
    sys.exit()

#!/usr/bin/env python3

# A socket is used to connect two nodes together.
# To connect to an open port and IP address
# This is a simple socket script and port connection
import socket

HOST = socket.gethostbyname(socket._LOCALHOST)  # 127.0.0.1 Localhost
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET = ipv4
# sock_stream = port
s.connect((HOST, PORT))

# use netcat = nc
# listening port = -nvlp

# nc -nvlp 7777

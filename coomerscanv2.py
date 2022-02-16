# Jacob Coomer
# This tool scans ports 1-65535 on a target address.
# This tool uses the socket, sys, and datetime packages.
# To run, use the command <py coomerscan.py ip>.
# You can break using Ctrl+C.

import socket
import sys
from datetime import datetime


# Scanning function
def connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    info = sock.connect_ex((host, port))
    if info == 0:
        print("Port " + str(port) + " Open -- " + str(datetime.now().time())[:8])
    sock.close()


# Check for IP argument in the command
if len(sys.argv) < 2:
    print("No target. Enter command in format <py coomerscan.py ip>")
    sys.exit()
target = sys.argv[1]

target = socket.gethostbyname(target)
try:  # try to scan all ports
    for i in range(1, 65356):
        connect(target, i)

except socket.gaierror:  # IP not valid
    print("Address information is not valid.")
    sys.exit()
except socket.error:  # Connection issue
    print("Unable to connect. Host may still be valid.")
    sys.exit()
except KeyboardInterrupt:  # User Exit
    print("Ctrl C -> Exit")
    sys.exit()

print("Done")
sys.exit()

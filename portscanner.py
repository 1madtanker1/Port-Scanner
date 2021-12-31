import pyfiglet
import sys
import subprocess
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("80")
print(ascii_banner)

a = input("Enter the Ip address you want to scan > ")
target = (a)

#ADDING BANNER TO DISPLAY RESULTS
print("-" * 50)
print("Scanning Target:" + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

###RETURNS IF PORT IS OPEN
        result = s.connect_ex((target, port))

        if result == 0:
            print("Port {} is open!". format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting the program")
    sys.exit()
except socket.gaierror:
    print("\n Could not resolve hostname")
    sys.exit()
except socket.error:
    print("\n Server not responding")
    sys.exit()

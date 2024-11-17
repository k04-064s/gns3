#!/usr/bin/env python3

import os
import subprocess

# Server information
SERVER_IP = "34.65.90.86"  # server IP
SERVER_USERNAME = "charalamposprh"
SERVER_KEY = os.path.expanduser("~/.ssh/id_rsa")  # server SSH private key path
USER_CODE = None

# List of IPs to ping
PING_IPS = [
    "10.1.1.1", "10.1.1.2", "10.1.2.1", "10.1.2.2",
    "10.1.3.1", "10.1.3.2", "109.99.99.1", "109.99.99.2"
]

# Ensure dependencies
def install_dependencies():
    print("Installing required dependencies...")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y telnet gcc sshpass")
    print("Dependencies installed.")

# Request user code
def get_user_code():
    global USER_CODE
    USER_CODE = input("Enter your unique 7-digit user code: ")
    if len(USER_CODE) != 7 or not USER_CODE.isdigit():
        print("Invalid code. Please restart and try again.")
        exit(1)
    print(f"User code {USER_CODE} accepted.")

# Ping the IPs
def local_ping_test():
    print("Starting local ping test...")
    for ip in PING_IPS:
        print(f"Pinging {ip}...")
        result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "1 received" in result.stdout:
            print(f"[{ip}] Ping Success!")
        else:
            print(f"[{ip}] Ping Failed!")

# Connect to the server
def connect_to_server():
    print("Connecting to the server...")
    try:
        ssh_command = (
            f"ssh -i {SERVER_KEY} {SERVER_USERNAME}@{SERVER_IP} "
            f"'python3 /path/to/server_script.py {USER_CODE}'"
        )
        os.system(ssh_command)
    except Exception as e:
        print(f"Error connecting to the server: {e}")

if __name__ == "__main__":
    install_dependencies()
    get_user_code()
    local_ping_test()
    connect_to_server()


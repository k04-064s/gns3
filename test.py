import os
import uuid
import socket
import subprocess

def get_user_id():
    user_id = input("Enter your unique user ID: ")
    return user_id

def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) 
                    for i in range(0, 2*6, 8)][::-1])
    return mac

def check_connectivity(ip_list):
    results = {}
    for ip in ip_list:
        response = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE)
        results[ip] = 'reachable' if response.returncode == 0 else 'unreachable'
    return results

def log_results(user_id, ip, mac, connectivity_results):
    with open("connectivity_log.txt", "a") as f:
        f.write(f"User ID: {user_id}\n")
        f.write(f"IP Address: {ip}\n")
        f.write(f"MAC Address: {mac}\n")
        for ip, status in connectivity_results.items():
            f.write(f"{ip}: {status}\n")
        f.write("----------\n")

def main():
    user_id = get_user_id()
    ip = get_ip_address()
    mac = get_mac_address()
    ip_list = ['8.8.8.8', '192.168.1.1']  # Add relevant IPs to ping
    connectivity_results = check_connectivity(ip_list)
    log_results(user_id, ip, mac, connectivity_results)

if __name__ == "__main__":
    main()

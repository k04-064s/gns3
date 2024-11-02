import os
import subprocess
import platform
import socket
import requests

# List of IPs to test connectivity with
target_ips = ["10.1.1.1", "10.1.2.2", "109.99.99.1"]  # Replace with IPs in your topology

# Function to ping a host
def ping_host(ip):
    response = subprocess.run(
        ["ping", "-c", "1", ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return response.returncode == 0

# Get MAC address of a given network interface
def get_mac_address(interface="ens4"):
    try:
        with open(f"/sys/class/net/{interface}/address") as f:
            mac = f.read().strip()
        return mac
    except FileNotFoundError:
        return "Interface not found"

# Get local IP address
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Get system information
def get_system_info():
    sys_info = {
        "Hostname": socket.gethostname(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Platform": platform.platform()
    }
    return sys_info

# Write results to a file
def write_results_to_file(results):
    with open("network_test_results.txt", "w") as f:
        f.write("Network Test Results:\n")
        for line in results:
            f.write(line + "\n")

# Main function
def main():
    results = []

    # Test connectivity to each IP
    results.append("Ping Test Results:")
    for ip in target_ips:
        reachable = ping_host(ip)
        results.append(f"{ip}: {'Reachable' if reachable else 'Unreachable'}")

    # Get local IP and MAC address
    ip_address = get_ip_address()
    mac_address = get_mac_address()
    results.append(f"\nLocal IP Address: {ip_address}")
    results.append(f"MAC Address: {mac_address}")

    # Get system info
    sys_info = get_system_info()
    results.append("\nSystem Information:")
    for key, value in sys_info.items():
        results.append(f"{key}: {value}")

    # Write to file
    write_results_to_file(results)
    print("Network test results saved to 'network_test_results.txt'.")

if __name__ == "__main__":
    main()

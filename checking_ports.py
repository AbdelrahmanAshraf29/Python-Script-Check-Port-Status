import socket
from ipaddress import ip_address, IPv4Address


def generate_ip_range(start_ip, count):
    start = ip_address(start_ip)
    return [str(start + i) for i in range(count)]
# Define the starting IP and the number of servers
start_ip = "192.168.1.1"
num_servers = 10
# Generate the list of IPs
servers = generate_ip_range(start_ip, num_servers)



# Define the range of ports to scan
start_port = 75
end_port = 85

def check_port_status(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  
        result = s.connect_ex((ip, port))
        s.close()
        if result == 0:
            return "open"
        else:
            return "closed"
    except :
        print ("Time out")

# Check ports for each server
for server in servers:
    print(f"Checking ports on server {server}:")
    for port in range(start_port, end_port + 1):
        status = check_port_status(server, port)
        print(f"Port {port}: {status}")
    print()  # Print an empty line for separation between servers

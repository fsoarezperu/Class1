import socket
import ipaddress

def scan_port(ip, port):
    try:
        socket.create_connection((ip, port), timeout=1)
        return True
    except OSError:
        return False

def scan_ip(ip):
    open_ports = []
    for port in range(1, 1025):
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports

ip = input("please enter an ip address:")

#ip = "192.168.0.1"
open_ports = scan_ip(ip)
print(f"The open ports on {ip} are: {open_ports}")

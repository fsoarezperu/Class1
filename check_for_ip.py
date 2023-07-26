import re

def find_ip(text):
    pattern = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    return re.findall(pattern, text)

given_text = input("paste the text you need to scan for ip´s:")
#text = "this are valid IP addresses: 192.168.0.1, 10.0.0.1, 255.255.255.255. And this are NOT : 256.0.0.0."
ips = find_ip(given_text)
for ip in ips:
    print(".".join(ip))


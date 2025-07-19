from ipaddress import ip_network

network = ip_network('235.86.56.0/21')

count = 0
for ip in network:
    if (int(ip) & 0b11) == 0b11:
        count += 1
print(count)

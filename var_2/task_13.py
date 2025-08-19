from ipaddress import ip_network

ip = '93.138.164.49'
target_network = '93.138.160.0'

mask = []
for i in range(33):
    net = ip_network(f'{ip}/{i}', strict = False)
    if str(net.network_address) == target_network:
        mask.append(str(net.netmask))

for n in mask:
    print(n)
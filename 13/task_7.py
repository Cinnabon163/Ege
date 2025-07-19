from ipaddress import ip_address, ip_network

ip = ip_address('215.181.200.27')
target_network = '215.181.192.0'



for i in range (33):
    net = ip_network(f'{ip}/{i}', strict = False)
    if str(net.network_address) == target_network:
        mask = net.netmask.packed
        third_byte = mask[2]
        print(f"{third_byte} ({net.netmask})")
        
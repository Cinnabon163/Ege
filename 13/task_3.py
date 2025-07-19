#from ipaddress import ip_address, ip_network

#ip = ip_address('158.116.11.146')
#target_network = '158.116.0.0'

#count = 0

# for i in range (33):
    net = ip_network(f'{ip}/{i}', strict = False)
    if str(net.network_address) == target_network:
        count += 1
    else:
        break

#print(count)

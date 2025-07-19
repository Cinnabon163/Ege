from ipaddress import ip_address, ip_network

ip = ip_address('172.16.160.0')
mask = '255.255.240.0'

net = ip_network(f'{ip}/{mask}', strict = False)
count = 0
for i in range(33):
    if str(bin(int(ip))).count('1') % 4 != 0:
        count += 1
print(count)


    




    

        
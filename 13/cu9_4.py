from ipaddress import ip_network
counter = 0
for i in ip_network('122.159.136.144/255.255.255.248'):
    if f"{i:b}".count("1") % 4:
        counter += 1
print(counter)
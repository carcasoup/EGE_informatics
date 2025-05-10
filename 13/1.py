from ipaddress import ip_network
for i in ip_network("98.81.154.195/255.252.0.0", 0):
    print(i)
"""
Ответ: 9883255255
"""
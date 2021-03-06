#!/usr/bin/python3

import requests

nodes = ['139.162.172.252', '82.8.59.60', '139.162.181.204', '91.107.104.167', '212.83.176.26', '193.124.182.113', '46.228.6.34', '84.238.148.25', '104.198.8.205', '104.250.143.14', '77.174.135.61', '139.162.172.167', '95.183.48.178', '93.186.255.245', '69.30.201.234', '195.91.176.86', '163.172.144.233', '159.203.187.109', '52.51.92.182', '104.236.219.81', '139.59.213.17', '45.63.89.38', '52.30.47.67', '139.59.165.114', '178.21.112.50', '96.84.69.81', '130.211.76.69', '190.10.8.74', '163.172.158.246', '104.198.2.225', '85.255.4.208', '86.93.11.119', '94.214.44.158', '178.21.118.37', '138.201.91.160', '130.211.240.10', '137.74.112.39', '81.88.208.178', '178.218.117.66', '51.255.212.134', '52.77.111.219', '94.127.219.245', '193.124.182.134', '178.79.164.220', '159.203.186.143', '51.255.46.133', '104.154.57.29', '23.94.190.226', '138.201.247.72', '81.88.208.180', '84.22.115.12', '195.37.209.147', '139.59.185.243', '87.106.15.184', '190.10.8.150', '52.28.66.217', '193.124.182.142', '193.172.33.72', '178.21.112.237', '137.74.112.73', '31.43.101.66']
newnodes = set()

for node in nodes:
    try:
        r = requests.get("http://" + node + ":6869/peers/connected", timeout=2)
        data = r.json()
        for newnode in data['peers']:
            addr = newnode['address']
            print(addr.split('/')[1].split(':')[0])
            newnodes.add(addr.split('/')[1].split(':')[0])
    except: pass
    print(str(len(newnodes)) + "/" + str(len(nodes)), "nodes:", list(newnodes))
    for node in newnodes:
        print("\"%s:6863\"," % node, end="")
    print()


#!/usr/bin/python3

import etcd3
import json

etcd = etcd3.client(host='192.168.147.60', port=2379)

inventory = {"_meta": {}}

hosts = [m.key for (_, m) in etcd.get_all()]
for host in hosts:
    for role in json.loads(etcd.get(host)[0].decode()):
        if role not in inventory.keys():
            inventory[role] = {}
            inventory[role]['hosts'] = []
        inventory[role]['hosts'].append(host.decode())

print(json.dumps(inventory))
#!/usr/bin/python3

import etcd3
import json

etcd = etcd3.client(host='192.168.0.154', port=2379)

inventory = {}
inventory["_meta"] = {}
inventory["_meta"]["hostvars"] = {}

for (_, m) in etcd.get_all():
    for role in etcd.get(m.key)[0].decode().split(','):
        hostname = m.key.decode()
        if role not in inventory.keys():
            inventory[role] = {}
            inventory[role]['hosts'] = []
        inventory[role]['hosts'].append(hostname)

print(json.dumps(inventory))

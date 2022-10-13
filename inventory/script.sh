#!/usr/bin/python3

import etcd3
import json
etcd = etcd3.client(host='192.168.0.154', port=2379)

inventory = {}
inventory["all"] = {}
inventory["all"]["hosts"] = []

roles = {}
for (_,m) in etcd.get_all():
     for role in etcd.get(m.key)[0].decode().split(','):
            inventory["all"]["hosts"].append(m.key.decode())
            if role not in roles.keys():
                    roles[role] = {}
                    roles[role]['hosts'] = {}
                    roles[role]['vars'] = {}
            roles[role]['hosts'][m.key.decode()] = None
            if role in ["gearman-ansible"]:
                    roles[role]["vars"]["gearman_job"] = "ansible"
            if role in ["gearman-etcd"]:
                    roles[role]["vars"]["gearman_job"] = "inventory"
inventory["all"]["children"] = roles

print(json.dumps(inventory))
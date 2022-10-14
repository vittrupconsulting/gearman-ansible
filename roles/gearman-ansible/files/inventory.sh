#!/usr/bin/python3

import etcd3
import json
etcd = etcd3.client(host='192.168.0.154', port=2379)

roles = {}
roles["_meta"] = {}
roles["_meta"]["hostvars"] = {}

for (_,m) in etcd.get_all():
     for role in etcd.get(m.key)[0].decode().split(','):
            if role not in roles.keys():
                    roles[role] = {}
                    roles[role]['hosts'] = []
            roles[role]['hosts'].append(m.key.decode())
            if role in ["gearman-ansible"]:
                    roles["_meta"]["hostvars"][m.key.decode()] = {}
                    roles["_meta"]["hostvars"][m.key.decode()]["gearman_job"] = "ansible"
            if role in ["gearman-etcd"]:
                    roles["_meta"]["hostvars"][m.key.decode()] = {}
                    roles["_meta"]["hostvars"][m.key.decode()]["gearman_job"] = "inventory"

print(json.dumps(roles))
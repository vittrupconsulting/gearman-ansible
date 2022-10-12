#!/usr/bin/python3

import json
import etcd3

f = open('/etc/ansible/facts.d/roles.fact')
roles = json.load(f)
f.close()

etcd = etcd3.client()
etcd.put("server1", json.dumps(roles))
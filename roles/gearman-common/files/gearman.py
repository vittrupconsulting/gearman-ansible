#!/usr/bin/python3

import gear
import sys
import random
import json

f = open('/etc/ansible/facts.d/servers.fact')
servers = json.load(f)
f.close()
random.shuffle(servers)

client = gear.Client()
for server in servers:
    print(f"{server}", "4730")
    client.addServer(f"{server}", "4730")
client.waitForServer()

job = gear.Job("ansible", sys.argv[1].encode("UTF-8"))
client.submitJob(job)

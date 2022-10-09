#!/usr/bin/python3

import gear
import sys
import random
import json

from gear import TimeoutError

f = open('/etc/ansible/facts.d/servers.fact')
servers = json.load(f)
f.close()
random.shuffle(servers)

client = gear.Client()
for server in servers:
    print(f"Gearman server {server}")
    client.addServer(f"{server}", "4730")

try:
    client.waitForServer(60)
    job = gear.Job("common", sys.argv[1].encode("UTF-8"))
    client.submitJob(job)
except TimeoutError:
    print("All gearman servers offline.")
else:
    print("Found online gearman server.")

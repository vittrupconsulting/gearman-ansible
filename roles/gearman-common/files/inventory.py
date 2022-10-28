import sys
import gear
import json
import socket
import random

f = open('/etc/ansible/facts.d/gearman.fact')
servers = json.load(f)
f.close()

r = open('/etc/ansible/facts.d/roles.fact')
roles = json.load(r)
r.close()

random.shuffle(servers)

client = gear.Client()
for server in servers:
    client.addServer(f"{server}", 4730)

try:
    client.waitForServer(60)
    payload = {}
    payload["source"] = socket.gethostname()
    payload["roles"] = roles
    job = gear.Job("inventory", bytes(json.dumps(payload), 'utf-8'))
    client.submitJob(job)
except TimeoutError:
    sys.exit(1)
else:
    sys.exit(0)

import sys
import gear
import json
import socket
import random

f = open('/etc/ansible/facts.d/gearman.fact')
servers = json.load(f)
f.close()

random.shuffle(servers)

client = gear.Client()
for server in servers:
    client.addServer(f"{server}", 4730)

try:
    client.waitForServer(60)
    job = gear.Job("ansible", bytes(json.dumps({"source": socket.gethostname()}), 'utf-8'))
    client.submitJob(job)
except TimeoutError:
    sys.exit(1)
else:
    sys.exit(0)

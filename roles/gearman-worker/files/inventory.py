import gear
from etcd3 import Client
import json
from systemd import journal

f = open('/etc/ansible/facts.d/servers.fact')
servers = json.load(f)
f.close()

worker = gear.Worker('inventory')
for server in servers:
    worker.addServer(f"{server}")
worker.registerFunction("register")

client = Client('127.0.0.1', 2379)

while True:
    job = worker.getJob()
    name = f"{job.arguments.decode().split()[0]}"
    #get source from job?
    groups = f"{job.arguments.decode().split()[1]}"
    journal.send(f"Storing {name}==>{groups}")
    client.put(name, groups)
    job.sendWorkComplete()

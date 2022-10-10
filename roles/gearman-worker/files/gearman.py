import gear
from etcd3 import Client
import subprocess
from systemd import journal
import json

f = open('/etc/ansible/facts.d/servers.fact')
servers = json.load(f)
f.close()

worker = gear.Worker(f"sample")
for server in servers:
    journal.send(f"Gearman server {server}")
    worker.addServer(f"{server}")
worker.registerFunction("common")

client = Client('127.0.0.1', 2379)

while True:
    job = worker.getJob()
    journal.send(f"Gearman client {job.arguments.decode()}")
    client.put(f"{job.arguments.decode()}", f"{job.arguments.decode()}")
    subprocess.run(f"ansible-playbook --inventory '{job.arguments.decode()},' /etc/ansible/common.yml", shell=True)
    job.sendWorkComplete()

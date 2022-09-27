import sys
import gear
import subprocess
from systemd import journal
import socket

worker = gear.Worker(f"{socket.gethostname()}")
for server in sys.argv[1:]:
    journal.send(f"Gearman server {server}")
    worker.addServer(f"{server}")
worker.registerFunction("ansible")

while True:
    job = worker.getJob()
    journal.send(f"Gearman client {job.arguments.decode()}")
    subprocess.run(f"ansible-playbook -i '{job.arguments.decode()},' /etc/ansible/common.yml", shell=True)
    job.sendWorkComplete()

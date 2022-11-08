import sys
import gear
import json
import socket

client = gear.Client()
client.addServer("192.168.147.60", 4730)

try:
    client.waitForServer(60)
    inventory = gear.Job("inventory", bytes(json.dumps({"source": socket.gethostname(), "roles": ["ungrouped"]}), 'utf-8'))
    client.submitJob(inventory)
    ansible = gear.Job("ansible", bytes(json.dumps({"source": socket.gethostname()}), 'utf-8'))
    client.submitJob(ansible)

except TimeoutError:
    sys.exit(1)
else:
    sys.exit(0)

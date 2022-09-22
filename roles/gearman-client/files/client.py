import gear
import sys

client = gear.Client()
client.addServer('172.16.1.15')
client.waitForServer()

job = gear.Job('ansible', sys.argv[1].encode("UTF-8"))
client.submitJob(job)

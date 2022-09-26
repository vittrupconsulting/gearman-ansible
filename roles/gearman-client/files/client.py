#!/usr/bin/python3

import gear
import sys

client = gear.Client()
client.addServer(sys.argv[2].encode("UTF-8"), sys.argv[4].encode("UTF-8"))
client.waitForServer()

job = gear.Job(sys.argv[6].encode("UTF-8"), sys.argv[7].encode("UTF-8"))
client.submitJob(job)

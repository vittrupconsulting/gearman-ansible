import gear
import subprocess
worker = gear.Worker('ansible')
worker.addServer('172.16.1.10')
worker.addServer('172.16.1.11')
worker.registerFunction("ansible")

while True:
    job = worker.getJob()
    print(f'>>{job.arguments}<<')
    #print(f"ansible --inventory '{job.arguments.decode()},'")
    #print(subprocess.run(f"a{job.arguments}", shell=True))
    job.sendWorkComplete()

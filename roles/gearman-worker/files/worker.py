import gear
import subprocess
import logging
from systemd import journal

worker = gear.Worker('ansible')
worker.addServer('172.16.1.10')
worker.registerFunction("ansible")

# logger = logging.getLogger('custom_logger_name')
# logger.addHandler(journal.JournalHandler(SYSLOG_IDENTIFIER='custom_unit_name'))
# logger.warning("1Some message: %s", 'detail')
# logger.debug("2Some message: %s", 'detail')
# logger.error("3Some message: %s", 'detail')
# logger.critical("4Some message: %s", 'detail')

while True:
    job = worker.getJob()
#    print(f'>>{job.arguments}<<')
    journal.send(f"Server {job.arguments.decode()}")
    #print(f"ansible --inventory '{job.arguments.decode()},'")
    #print(subprocess.run(f"a{job.arguments}", shell=True))
    job.sendWorkComplete()

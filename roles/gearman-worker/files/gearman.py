import sys
import gear
import subprocess
import logging
from systemd import journal
import socket

worker = gear.Worker(f"{socket.gethostname()}")
for server in sys.argv[1:]:
    journal.send(f"Gearman server {server}")
    worker.addServer(f"{server}")
worker.registerFunction("ansible")

# logger = logging.getLogger('custom_logger_name')
# logger.addHandler(journal.JournalHandler(SYSLOG_IDENTIFIER='custom_unit_name'))
# logger.warning("1Some message: %s", 'detail')
# logger.debug("2Some message: %s", 'detail')
# logger.error("3Some message: %s", 'detail')
# logger.critical("4Some message: %s", 'detail')

while True:
    job = worker.getJob()
    journal.send(f"Gearman client {job.arguments.decode()}")
#    subprocess.run(f"whoami", shell=True)
    subprocess.run(f"ansible-playbook -i '{job.arguments.decode()},' /etc/ansible/common.yml", shell=True)
    job.sendWorkComplete()

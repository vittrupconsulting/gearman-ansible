import sys
import gear
import subprocess
import logging
from systemd import journal

worker = gear.Worker('ansible')
for server in sys.argv[1:]:
    journal.send(f"Registering {server}")
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
    journal.send(f"Server {job.arguments.decode()}")
    subprocess.run(f"sudo ansible-playbook /etc/ansible/roles/gearman-worker/tests/test.yml", shell=True)
    job.sendWorkComplete()

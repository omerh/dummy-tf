import tensorflow as tf
import time
import logging
from systemd import journal

log = logging.getLogger('demo')
log.addHandler(journal.JournaldLogHandler())
log.setLevel(logging.INFO)


def main():
    while True:
        log.info("start")
        time.sleep(5)
        log.info(tf.__version__)
        
        
if __name__ == "__main__":
    log.info("sent to journal")
    main()


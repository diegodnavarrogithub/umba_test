import logging

class Logging_help:
    def __init__(self):
        FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
        logging.basicConfig(filename="activity_logs.log", level=logging.DEBUG, format=FORMAT)
        d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
        logger = logging.getLogger('tcpserver')
        self.log = logger

        # logger.warning('Protocol problem: %s', 'connection reset', extra=d)
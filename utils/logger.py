import logging
import os
from pathlib import Path


class Logger:

    @staticmethod
    def log():
        _path = os.path.join(Path(__file__).absolute().parent.parent, 'logs')
        if not os.path.exists(_path):
            os.makedirs(_path)
        logging.basicConfig(filename=os.path.join(_path, 'test_run.log'), format='%(asctime)s: %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

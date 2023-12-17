import logging
import os
from pathlib import Path


class Logger:

    @staticmethod
    def log():
        _path = os.path.join(Path(__file__).absolute().parent.parent, 'logs', 'test_run.log')
        logging.basicConfig(filename=_path, format='%(asctime)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

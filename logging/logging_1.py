import logging
from pathlib import Path
from base_logging import set_logger

if __name__ == '__main__':
    logger = set_logger(__file__)

    logger.debug(
        '%s - %s',
        100,
        'abc'
    )

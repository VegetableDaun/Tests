import logging
from pathlib import Path
from logging import Logger
def set_logger(name: str) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.DEBUG)

    file_path = Path(name)
    handler = logging.FileHandler(
        filename=f'{file_path}.log',
        encoding='utf-8'
    )
    handler.setLevel(level=logging.DEBUG)

    formatter = logging.Formatter(
        fmt="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
def set_logging_base_config(level=logging.DEBUG) -> None:
    file_path = Path(__name__).name

    logging.basicConfig(
        level=level,
        encoding='utf-8',
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s: %(message)s",
        filename=f'{file_path}.log',
    )

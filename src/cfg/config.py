import logging
import json

from logging.handlers import RotatingFileHandler
from loguru import logger


def setup_logger(name: str, log_file: str, level=logging.ERROR, max_bytes=10485760, backup_count=3):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setFormatter(formatter)
    handler.setLevel(level)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def load_config(config_file: str):
    with open(config_file) as cfg_file:
        config = json.load(cfg_file)
        loggers = {}
        for logger_name, logger_config in config.items():
            loggers[logger_name] = setup_logger(
                logger_name,
                logger_config["log_file"],
                getattr(logging, logger_config["level"].upper(), logging.ERROR),
                logger_config.get("max_bytes", 10485760),
                logger_config.get("backup_count", 3)
            )
        return loggers


# Загрузка конфигурации логгеров
loggers = load_config('src/cfg/logging_config.json')
error_logger = loggers.get('error_logger')
info_logger = loggers.get('info_logger')
warning_logger = loggers.get('warning_logger')
success_logger = loggers.get('success_logger')
debug_logger = loggers.get('debug_logger')


def load_config(config_file: str):
    with open(config_file, 'r') as file:
        config = json.load(file)
        for sink in config["sinks"]:
            logger.add(
                sink["log_file"],
                level=sink["level"],
                rotation=sink.get("rotation", "10 MB"),
                retention=sink.get("retention", "3 files"),
                format="{time} - {name} - {level} - {message}"
            )


# Загрузка конфигурации логгеров
load_config('src/cfg/loguru_config.json')
my_logger = logger

import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name: str, log_file: str, level=logging.ERROR, max_bytes=10485760, backup_count=3):
    """Создает и настраивает логгер с заданным именем, файлом логов, уровнем логирования и ротацией логов."""
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setFormatter(formatter)
    handler.setLevel(level)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# Настройка логгеров с различными уровнями логирования
error_logger = setup_logger('error_logger', 'src/data/common_log.log', level=logging.ERROR)
info_logger = setup_logger('info_logger', 'src/data/common_log.log', level=logging.INFO)
warning_logger = setup_logger('warning_logger', 'src/data/common_log.log', level=logging.WARNING)
success_logger = setup_logger('success_logger', 'src/data/common_log.log', level=logging.INFO)
debug_logger = setup_logger('debug_logger', 'src/data/debug_log.log', level=logging.DEBUG)

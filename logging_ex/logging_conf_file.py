import logging.config

logging.config.fileConfig("logging.conf")

logger = logging.getLogger("simpleExample")

logger.debug("This is a debug message")

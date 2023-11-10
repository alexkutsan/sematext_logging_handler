import logging
import sys

from sematext_logging_handler import SematextHandler

def setup_log(logger_name, 
              sematext_url,
              sematext_app_token,
              log_level=logging.DEBUG, 
              stdout_format = '%(asctime)s - %(name)s [%(levelname)s] - %(message)s',
              other_loggers_level=None,
              root_logger_level=logging.INFO):
    if root_logger_level:
        logging.root.setLevel(root_logger_level)
    logger = logging.getLogger(logger_name)
    logger.propagate = False
    logger.setLevel(log_level)
    
    if stdout_format:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(log_level)
        formatter = logging.Formatter(stdout_format)
        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)
        if root_logger_level:
            logging.root.addHandler(stdout_handler)
        
    
    sematext_handler = SematextHandler(host=sematext_url, logsene_app_token=sematext_app_token)
    sematext_handler.setLevel(log_level)
    logger.addHandler(sematext_handler)
    if root_logger_level:
        logging.root.addHandler(sematext_handler)
    
    if other_loggers_level:
        for name, log in logging.root.manager.loggerDict.items():
            if name != logger_name:
                log.setLevel(other_loggers_level)

    return logger
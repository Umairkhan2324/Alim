import logging
import sys
import os

def get_logger(name: str):
    """
    Configures and returns a logger.
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent the logger from propagating to the root logger
    logger.propagate = False

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    # Console handler
    stream_handler = logging.StreamHandler(sys.stdout)
    
    # File handler
    file_handler = logging.FileHandler(os.path.join(log_dir, "app.log"))
    
    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger 
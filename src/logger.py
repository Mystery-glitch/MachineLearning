# In Python, a logger is an object provided by the logging module that is used to record the log messages.

import logging
import os
from datetime import datetime

# creates a log file if dosen't exits
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# full path to the log file
LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

# configure the logger, i.e., save logs to the file path specified, also specifies how the log message will appear.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
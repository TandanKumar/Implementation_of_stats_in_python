import logging
from datetime import datetime
import os
import pandas

LOG_DIR = "logfile"

def get_log_file_name():
    return f"log_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"

Log_FILE_NAME = get_log_file_name()

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,Log_FILE_NAME)

logging.basicConfig(filename= LOG_FILE_PATH, 
filemode ="w",
format='[%(asctime)s]^;%(levelName)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level= logging.INFO                    
)

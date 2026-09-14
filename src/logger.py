'''
    The purpose of this file is to create a logging info tracker, 
    where whenever you do something, whether you run the program, 
    you raise and error and more, you log that info in a file. 

    looger.py will create a log file to keep track of 
    steps in project, such as errors, changes and more. 

    Ex: test.log: 
        Logging Settings

        Save file:
        ------------------------
        logs/07_26_2026.log

        Format:
        ------------------------
        time
        line number
        message

        Minimum level:
        ------------------------
        INFO

        It builds the skeleton using logging.basicConfig() and then later
        in other files we do lpogging.info("Training started.")

    Steps: 
        1. Make the log file name
        2. Make the log folder path
        3. Make the full path to log file
        4. Configure the logger using logging.basicConfig()

    Functions used: 
        1. datetime.now(): gets the current date and time.
        2. .strftime(...): turns that date and time into formatted text.
            %m  month, %d  day, %Y  four-digit year, %H  hour, %M  minute, %S  second
        3. os.path.joins(...): Combines path pieces safely.
            Ex: os.path.join(os.getcwd(), "logs") -> /Users/adrina/ML_Project/logs
        4. os.makedirs(logs_path, exist_ok=True): Create the logs folder.   
'''

import logging
import os
from datetime import datetime

# Make the name of log file: 
LOG_FILENAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Make the path of log folder: 
logs_folder_path = os.path.join(os.getcwd(), "logs")

# Make the folder using the path
os.makedirs(logs_folder_path, exist_ok=True)

# Make the log file path, using the folder path, and log name
LOG_FILE_PATH = os.path.join(logs_folder_path, LOG_FILENAME)

# Save logging messages into this file (send the filepath)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=(
        "[ %(asctime)s ] "
        "line %(lineno)d "
        "%(name)s - "
        "%(levelname)s - "
        "%(message)s"
    ),
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
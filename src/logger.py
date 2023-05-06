import logging
import os
from datetime import datetime


# creates a filename for the log file - current date and time
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

 # path where the log file will be stored: "root/logs/filename.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# Add the "logs" folder in the current working directory, if it doesn't 
# exist already. "exist_ok=True" is used to avoid error if folder already exists.
os.makedirs(logs_path,exist_ok=True)

# creates the full path of the log file by joining the logs_path and LOG_FILE.
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)



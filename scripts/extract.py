import pandas as pd
import snscrape
import logging
import logging.config
from datetime import datetime



def setup_logging():

    CONFIG_DIR = "./config"
    LOG_DIR = "./logs"
    
    file_name = "logging.ini"
    config_path = "/".join([CONFIG_DIR, file_name])
    timestamp = datetime.now().strftime("%Y%M%d-%H-%M-%S")
    
    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=True,
        defaults={"filename": f"{LOG_DIR}/{timestamp}.log"}
    )


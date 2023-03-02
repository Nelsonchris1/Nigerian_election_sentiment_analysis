import logging
import logging.config
from datetime import datetime
from os import path
from typing import List

import pandas as pd
import snscrape.modules.twitter as sntwitter


def setup_logging():
    CONFIG_DIR = "config"
    LOG_DIR = "logs"

    file_name = "logging.ini"
    config_path = "/".join([CONFIG_DIR, file_name])
    timestamp = datetime.now().strftime("%Y%M%d-%H-%M-%S")
    # log_file_path = path.join(path.dirname(path.abspath(__file__)), config_path)

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=True,
        defaults={"logfilename": f"{LOG_DIR}/{timestamp}.log"},
    )


def pull_data(query:str, file_name: str) -> pd.DataFrame:

    tweets = []

    limit = 10000
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if len(tweets) == limit:
                break
            else:
                tweets.append(
                    [
                        tweet.date,
                        tweet.sourceLabel,
                        tweet.rawContent,
                    ]
                )

    df = pd.DataFrame(
            tweets, columns=["Date", "Device", "Tweets"]
        )
    df.to_csv(f"data/election_{file_name}.csv", index=False)
        


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)

    query1 = "peter obi labour party -tinubu -atiku until:2023-02-25 since:2023-02-21"
    query2 = "tinubu apc -peter -obi -atiku -labour -party -PETER -OBI -PeterObi -Peter until:2023-02-25 since:2023-02-21"
    query3 = "atiku pdp -peter -obi -tinubu -Tinubu -labour -party -PETER -PeterObi -OBI -Peter until:2023-02-25 since:2023-02-21"

    logging.info("Starting Extraction")
    pull_data(query=query1, file_name="peter_obi")
    logging.info("Done extracting peter obi")

    pull_data(query=query2, file_name="tinubu")
    logging.info("Done extracting tinubu")

    pull_data(query=query3, file_name="atiku")
    logging.info("Done extracting atiku")
    logging.info("Done extracting all files")
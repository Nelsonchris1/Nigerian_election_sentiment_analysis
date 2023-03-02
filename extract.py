import logging
import logging.config
from datetime import datetime
from typing import List
from os import path
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


def pull_data(until: str, since: str) -> pd.DataFrame:


    query = {
        "peter_obi": f"peter obi labour party -tinubu -atiku until:{until} since:{since}",
        "tinubu": f"tinubu apc -peter -obi -atiku -labour -party -PETER -OBI -Peter until:{until} since:{since}",
        "atiku": f"atiku pdp -peter -obi -tinubu -Tinubu -labour -party -PETER -OBI -Peter until:{until} since:{since}",
    }

    tweets = []

    limit = 10000
    for k, v in query.items():
        for tweet in sntwitter.TwitterSearchScraper(v).get_items():
            if len(tweets) == limit:
                break
            else:
                tweets.append(
                    [
                        tweet.date,
                        tweet.user,
                        tweet.sourceLabel,
                        tweet.content,
                        tweet.coordinates,
                        tweet.place,
                    ]
                )

        df = pd.DataFrame(
            tweets, columns=["Date", "User", "Tweets", "Device", "Coordinates", "Place"]
        )
        df.to_csv(f"data/election_{k}_{until}.csv", index=False)
        


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)

    logging.info("Starting Extraction")
    pull_data(until="2023-02-26", since="2023-02-21")
    logging.info("Done extracting")
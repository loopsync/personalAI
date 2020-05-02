#!/home/thenerdsuperuser/.local/share/virtualenvs/something-CdvUv4a3/bin/python3.7

import tweepy
#import logging
from creds import *
import os

#logger = logging.getLogger()


def create_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()

    except Exception as e:
        #logger.error("Error creating API", exc_info=True)
        raise e

    #logger.info("API created")
    return api


if __name__ == "__main__":
    create_api()
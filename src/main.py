import sys
import re
import bot_logic as bot
from loguru import logger

if len(sys.argv) == 7 :
    logger.debug("Scanning command line arguments!")

    TWEET_INTERVAL = sys.argv[1]
    FIREBASE_API_KEY = sys.argv[2]
    TWITTER_API_KEY = sys.argv[3]
    TWITTER_API_SECRET = sys.argv[4]
    TWITTER_ACCESS_TOKEN = sys.argv[5]
    TWITTER_ACCESS_SECRET = sys.argv[6]

    logger.debug("Checking tweet interval!")
    if re.match("^\d\d?[HhMm]$",TWEET_INTERVAL) == None :
        logger.error("The tweet interval must look like this: 1h or 45m!")
    else : 
        logger.info("Bot is booting!")
        # TODO Start bot logic
else :
    logger.error('Missing arguments!')
    logger.error('Usage: main.py <TWEET-INTERVAL> <FIREBASE-API-KEY> <TWITTER-API-KEY> <TWITTER-API-SECRET> <TWITTER-ACCESS-TOKEN> <TWITTER-ACCESS-SECRET>')

input("\nPress any key to exit!") 

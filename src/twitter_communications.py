import tweepy
from loguru import logger

client = None

def __init__(api_key, api_secret, access_token, access_secret) :  
    try :
        # This grants access to the Twitter API V2
        # Sadly the V2 API does not have proper direct message handling yet (for some stupid reason)
        # client = tweepy.Client(
        #     consumer_key=api_key,
        #     consumer_secret=api_secret,
        #     access_token=access_token,
        #     access_token_secret=access_secret
        # )

        auth = tweepy.OAuth1UserHandler(
            api_key,
            api_secret,
            access_token,
            access_secret
        )

        client = tweepy.API(auth)
        client.update_status("#Python Rocks!")

        logger.info('Connected to twitter!')

    except Exception as e:
        # Just print(e) is cleaner and more likely what you want,
        # but if you insist on printing message specifically whenever possible...
        logger.error('Unable to connect to twitter!')
        if hasattr(e, 'message'):
            logger.error("Error message: " +e.message)
        else:
            logger.error(e) 

def get_new_messages() :
    toReturn = []
    logger.info("Trying to get direct messages")
    messages = client.get_direct_messages(count = 50, cursor = -1)

    for m in messages:
        logger.info(m.message_create.message_data.text)

        

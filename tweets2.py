import tweepy
from tweepy import TweepyException
api_key = ""
api_secret = ""
bearer_token = "%"
access_token = "-"
access_token_secret = ""


def create_api():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Create API object
    api = tweepy.API(auth)
    
    try:
        api.verify_credentials()
        print("Authentication OK")
    except TweepyException as e:
        print("Error during authentication")
        print(e)    

    return api

def tweet(api, message):
    try:
        api.update_status(message)
        print("Tweet successfully posted")
    except TweepyException as e:
        print("Error occurred while tweeting")
        print(e)

def main():
    api = create_api()
    tweet(api, "Hello Twitter from the API")

if __name__ == "__main__":
    main()

import tweepy
import webbrowser
from tweepy import TweepyException
api_key = ""
api_secret = ""
bearer_token = ""
access_token = ""
access_token_secret = ""

def create_api():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key, api_secret)

    # Redirect user for authorization
    try:
        redirect_url = auth.get_authorization_url()
        print("Please go here and authorize: ", redirect_url)
        webbrowser.open(redirect_url)
    except TweepyException as e:
        print('Error! Failed to get request token.')
        print(e)

    # Get access token
    verifier = input('Verifier:')

    try:
        auth.get_access_token(verifier)
    except TweepyException:
        print('Error! Failed to get access token.')

    # Create API object
    api = tweepy.API(auth)

    return api


def main():
    api = create_api()
    print("Successfully authenticated")
    client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
    auth = tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
    api = tweepy.API(auth)
    client.create_tweet(text= " from api ")
   # client.like("")

if __name__ == "__main__":
    main()

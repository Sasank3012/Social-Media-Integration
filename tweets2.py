import tweepy
from tweepy import TweepyException
api_key = "TCBON2h9x5NeFKXqCgRIYQJ1P"
api_secret = "87PIbBgDU2TwKkyu6zaVIo9SkVVnY5CykXYCP1Mvn7waeXtRYW"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIOuqgEAAAAA7GlMD852PT3bBKDgfAow5qLQ31M%3DTnrvBHHAf0Lk8NkeBliIfeKBNsvyNx2cd6Y8jl77eLmjgwKU3y"
access_token = "2317347446-MCdZzqRgccFaokBjo3Ln3kN2UxjQkgcifU1gqlJ"
access_token_secret = "ykNL42NIgoP3lc3BHr8mNhSCka9YVqWNA6ZJ639Ly3qmk"


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

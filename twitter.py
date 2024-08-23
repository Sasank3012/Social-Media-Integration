import tweepy

api_key = "TCBON2h9x5NeFKXqCgRIYQJ1P"
api_secret = "87PIbBgDU2TwKkyu6zaVIo9SkVVnY5CykXYCP1Mvn7waeXtRYW"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIOuqgEAAAAA7GlMD852PT3bBKDgfAow5qLQ31M%3DTnrvBHHAf0Lk8NkeBliIfeKBNsvyNx2cd6Y8jl77eLmjgwKU3y"
access_token = "2317347446-MCdZzqRgccFaokBjo3Ln3kN2UxjQkgcifU1gqlJ"
access_token_secret = "ykNL42NIgoP3lc3BHr8mNhSCka9YVqWNA6ZJ639Ly3qmk"

client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api = tweepy.API(auth)

#client.create_tweet(text= "hello world")
#client.retweet("1717244839891214544")
#client.like("1717244839891214544")
#client.create_tweet(in_reply_to_tweet_id="1717244839891214544",text="hey")
#for tweet in api.home_timeline():
#   print(tweet.text)
#person=client.get_user(username='narendramodi').data.id
#for tweet in client.get_users_tweets(person).data:
#    print(tweet.text)

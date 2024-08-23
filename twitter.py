import tweepy

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

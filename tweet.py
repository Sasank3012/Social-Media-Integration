import requests
import json

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def tweet(bearer_token, tweet):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    headers = create_headers(bearer_token)
    response = requests.post(url, headers=headers, params={"status": tweet})
    if response.status_code != 200:
        raise Exception("Error occurred: {} {}".format(response.status_code, response.text))
    return response.json()

def main():
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAGBxqgEAAAAAOMEBa0XOZ242DDy2lHdfLCU2v6U%3D9wKFXGAHo8o8eVx0xQNExx3q9cQDzHPVwBZoo4VUiMC5WjrE4U"
    tweet_text = "TWEET_TEXT"
    response = tweet(bearer_token, tweet_text)
    print(response)

if __name__ == "__main__":
    main()
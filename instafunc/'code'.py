'Code'
import re
import instaloader
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
# Loading the profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'sasank_30')
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)
# Creating an instance of Instaloader class
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
print("Emails extracted from the bio:")
print(emails)
# Provide the search query here
search_results = instaloader.TopSearchResults(bot.context, 'music')
# Iterating over the extracted usernames
for username in search_results.get_profiles():
    print(username)
# Iterating over the extracted hashtags
for hashtag in search_results.get_hashtags():
    print(hashtag)

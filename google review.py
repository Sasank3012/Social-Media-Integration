"""code"""
import json
import ssl
import requests

def get_place_id(api_key, place_name):
    """func"""
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_name}&inputtype=textquery&fields=place_id&key={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['candidates'][0]['place_id']

def get_reviews(api_key, place_id):
    """func"""
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,review&key={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['result']['reviews']

def parse_reviews(reviews):
    """func"""
    for review in reviews:
        print("Author name: ", review['author_name'])
        print("Review: ", review['text'])
        print("Time: ", review['relative_time_description'])
        print("\n")

def main():
    """main"""
    api_key = "YOUR_API_KEY"  
    place_name = "PLACE_NAME" 
    place_id = get_place_id(api_key, place_name)
    reviews = get_reviews(api_key, place_id)
    parse_reviews(reviews)

if __name__ == "__main__":
    main()
    

"""code"""
import os
import logging
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse: #pylint:disable=unused-argument
    """func"""
    logging.info('Python HTTP trigger function processed a request.')

    # Fetch the Page Access Token and Page ID from Azure Function App Settings
    page_access_token = ""
    page_id = ""

    # The message you want to post
    message = "new!"

    # The Graph API endpoint for posting to the feed
    post_url = f"https://graph.facebook.com/{page_id}/feed"

    # The data for the POST request
    payload = {
        "message": message,
        "access_token": page_access_token
    }

    # Make the POST request to the Graph API
    response = requests.post(post_url, params=payload,timeout=10)

    # Interpret the response
    if response.status_code == 200:
        return func.HttpResponse("Post was published on the Facebook page.")
    else:
        return func.HttpResponse(
            f"Failed to publish post: {response.text}",
            status_code=400
        )

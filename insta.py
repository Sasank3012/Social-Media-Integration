"""code"""
import requests
import azure.functions as func

def instafunc(req: func.HttpRequest) -> func.HttpResponse: #pylint:disable=unused-argument
    """The Instagram user ID and access token you got from the Facebook Developer portal"""
    ig_user_id = 'test126'
    ig_access_token = 'access code'#noqa

    # The URL of the image you want to post
    image_url = 'url'#noqa

    # The caption for the post
    caption = 'caption'

    # The endpoint for creating a new Instagram media object
    endpoint_url = f'https://graph.facebook.com/media'

    # The payload for the POST request
    payload = {
        'image_url': image_url,
        'caption': caption,
        'access_token': ig_access_token
    }

    # Send the POST request
    response = requests.post(endpoint_url, data=payload,timeout=5)

    # Return the response from the Instagram API
    return func.HttpResponse(response.text)

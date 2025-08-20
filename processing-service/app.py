import os
import requests
from flask import json
import redis
from urllib.parse import urlparse

redis_url = os.getenv("REDIS_CONNECTION_STRING", "redis://localhost:6379")
parsed_url = urlparse(redis_url)
r = redis.Redis(host=parsed_url.hostname, port=parsed_url.port, db=0)


def upload_to_imgur(image_url):
    """
    Upload an image to Imgur by URL
    Returns the Imgur URL if successful, None if failed
    """
    if not image_url:
        return None

    client_id = os.getenv("IMGUR_CLIENT_ID")
    if not client_id:
        print("IMGUR_CLIENT_ID not set in environment variables.")
        # TODO - Handle failures
        return None

    headers = {"Authorization": f"Client-ID {client_id}"}

    data = {"image": image_url, "type": "url"}

    try:
        response = requests.post(
            "https://api.imgur.com/3/image", headers=headers, data=data
        )
        response.raise_for_status()

        result = response.json()
        if result["success"]:
            return result["data"]["link"]
        else:
            print(f"Imgur upload failed: {result}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error uploading to Imgur: {e}")
        return None


while True:
    _, message = r.brpop("mylist")
    data = json.loads(message)
    print(f"Processing message: {data}")

    # Extract the image URL from the data
    image_url = data.get("image_url")

    if image_url:
        print(f"Uploading image to Imgur: {image_url}")
        imgur_url = upload_to_imgur(image_url)

        if imgur_url:
            print(f"Successfully uploaded to Imgur: {imgur_url}")
            # You can update the data with the new Imgur URL if needed
            data["imgur_url"] = imgur_url
        else:
            print("Failed to upload to Imgur")
    else:
        print("No image URL found in the data")

    # Continue with any other processing...

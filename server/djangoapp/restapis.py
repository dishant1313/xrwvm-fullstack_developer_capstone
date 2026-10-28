import os
import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
if not backend_url or "your" in backend_url.lower():
    backend_url = "http://localhost:3030"

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/"
)
if not sentiment_analyzer_url or "your" in sentiment_analyzer_url.lower():
    sentiment_analyzer_url = "http://localhost:5050/"


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + str(value) + "&"

    request_url = backend_url.rstrip('/') + endpoint
    if params:
        request_url = request_url + "?" + params.rstrip('&')

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url.rstrip('/') + "/analyze/" + text
    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred while analyzing sentiment: {err}")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    request_url = backend_url.rstrip('/') + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred while posting review: {err}")
        return None

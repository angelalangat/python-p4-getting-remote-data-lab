import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)
        return response.content  # Return the response body as bytes

    def load_json(self):
        response_body = self.get_response_body()  # Get the response body
        return json.loads(response_body)  # Parse the JSON and return as a Python object

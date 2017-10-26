import jsonify
import requests


class HttpClient(object):
    def get(self, url):
        response = requests.get(url)

        return json.loads(response.text)

import unittest
import requests
import responses
from mock3 import get_joke


class TestGetJoke(unittest.TestCase):
    
    @responses.activate
    def test_get_joke_returns_a_joke(self):
        responses.get(
            url='https://official-joke-api.appspot.com/jokes/random',
            json={
                'setup': 'Hello',
                'punchline': 'World'
            },
            status=403
        )

        self.assertEqual(get_joke(), 'HTTPError was raised')

    @responses.activate
    def test_get_joke_connection_error(self):
        responses.get(
            url='https://official-joke-api.appspot.com/jokes/random',
            body=requests.ConnectionError('ConnectionError was raised')
        )

        self.assertEqual(get_joke(), 'ConnectionError was raised')

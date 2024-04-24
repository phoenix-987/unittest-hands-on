import unittest
from mock1 import len_joke, get_joke
from unittest.mock import patch, MagicMock


class TestJoke(unittest.TestCase):
    
    @patch('mock1.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(), 3)

    @patch('mock1.requests')
    def test_get_joke(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'setup': 'Hello',
            'punchline': 'World'
        }

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(),'Hello\nWorld')

    @patch('mock1.requests')
    def test_fail_get_joke(self, mock_requests):

        mock_response = MagicMock(status_code=302)

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(),'No Jokes')


if __name__ == '__main__':
    unittest.main()

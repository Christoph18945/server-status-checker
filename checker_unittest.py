import unittest
from unittest.mock import patch
from io import StringIO
import checker

class TestWebsiteConnectivity(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def assert_output(self, expected_output, mock_stdout):
        with patch('checker.check_server_connectivity') as mock_check_connectivity:
            checker.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_valid_url(self):
        self.assert_output("Connected to https://www.example.com successfully. Status code: 200")

    def test_invalid_url(self):
        self.assert_output("Failed to connect to invalid_url. Error: Invalid URL 'invalid_url'")

    def test_non_string_url(self):
        with patch('sys.argv', ['checker.py', '123']):
            self.assert_output("123 is not a string!")

if __name__ == '__main__':
    unittest.main()

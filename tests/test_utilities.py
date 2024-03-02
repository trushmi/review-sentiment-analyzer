import unittest
from unittest.mock import patch, mock_open
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities

class TestUtilities(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="review1,\nreview2")
    def test_read_file(self, mock_file):
        result = utilities.read_file('test_file.txt')
        self.assertEqual(result, ['review1', 'review2'])
        mock_file.assert_called_once_with('test_file.txt', 'r')

    def test_preprocess_review(self):
        result = utilities.preprocess_review("This is a test review.")
        self.assertEqual(result, ['test', 'review'])

    def test_generate_features(self):
        result = utilities.generate_features(['review'], ['review'], 'Positive')
        self.assertEqual(result, [({'review': True}, 'Positive')])


if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch, mock_open
import sys
import os


os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value="This is a great product!")
    def test_main_positive(self, input):
        print(f"\nReview: {input.return_value}")
        main.main()

    @patch('builtins.input', return_value="This product is terrible.")
    def test_main_negative(self, input):
        print(f"\nReview: {input.return_value}")
        main.main()

    @patch('builtins.input', return_value="Easy to setup and very comfortable.")
    def test_main_specific_review(self, input):
        print(f"\nReview: {input.return_value}")
        main.main()

    @patch('builtins.input', return_value="So greatly disappointed in this purchase! Only had since September 6th, my husband weighs 155 and this chair is already pulling at the seams so severely that we will never be able to use! How disappointing! DO NOT BUY!")
    def test_main_specific_review(self, input):
        print(f"\nReview: {input.return_value}")
        main.main()

if __name__ == '__main__':
    unittest.main()
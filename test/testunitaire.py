import unittest
from io import StringIO
import sys
from main import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        fizzbuzz(15)

        sys.stdout = sys.stdout
        output = captured_output.getvalue().splitlines()

        expected_output = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "Fizzbuzz"
        ]
        self.assertEqual(output, expected_output)

if __name__ == 'main':
    unittest.main()

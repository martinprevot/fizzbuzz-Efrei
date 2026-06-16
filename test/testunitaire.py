import unittest
from io import StringIO
import sys
from main import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            fizzbuzz(15)
        finally:
            sys.stdout = original_stdout

        output = captured_output.getvalue().splitlines()

        expected_output = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
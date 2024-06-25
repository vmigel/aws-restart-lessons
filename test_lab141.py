import unittest
import os

# Import the functions from your script
from lab141 import is_prime, get_primes_between, save_primes_to_file

class TestPrimeFunctions(unittest.TestCase):

    def test_is_prime(self):
        """Test the is_prime function."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(9))

    def test_get_primes_between(self):
        """Test the get_primes_between function."""
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(get_primes_between(1, 100), expected_primes)

        expected_primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        self.assertEqual(get_primes_between(100, 200), expected_primes)

    def test_save_primes_to_file(self):
        """Test the save_primes_to_file function."""
        primes = [2, 3, 5, 7]
        file_path = 'test_results.txt'
        save_primes_to_file(primes, file_path)

        # Check if the file is created
        self.assertTrue(os.path.exists(file_path))

        # Read the file and verify its contents
        with open(file_path, 'r') as file:
            content = file.read().splitlines()
            self.assertEqual(content, ['2', '3', '5', '7'])

        # Clean up the test file
        os.remove(file_path)

if __name__ == "__main__":
    unittest.main()

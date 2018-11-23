"""Tests for example_django_app"""
import unittest
from example_django_app import return_a_string

class ExampleDjnagoAppTestCase(unittest.TestCase):
    """Test class for `example_django_app`."""

    def test_string_returning(self):
        """Does return_a_string() return expected string?"""
        self.assertEqual(return_a_string('test'), 'This is example_django_app returning: test')

if __name__ == '__main__':
    unittest.main()
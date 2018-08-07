import unittest
from doctest_usecase_1 import multiply

class simple_test(unittest.TestCase):

	@classmethod
	def setUpClass(self):
                print "--- DEBUG: Setup"

	def test_number_3_4(self):
                print "test_number_3_4"
		self.assertEqual(multiply(3,4),12)

	def test_string_a_3(self):
                print "test_string_a_3"
		self.assertEqual(multiply('a',3),'aaa')


if __name__ == '__main__':
	unittest.main()

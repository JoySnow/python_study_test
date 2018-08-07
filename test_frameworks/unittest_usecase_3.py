import unittest
from doctest_usecase_1 import multiply

def setUpModule():
        print "--- DEBUG: Setup"



class simple_test(unittest.TestCase):

	def test_number_3_4(self):
                print "test_number_3_4"
		self.assertEqual(multiply(3,4),12)

	def test_string_a_3(self):
                print "test_string_a_3"


class simple_test2(unittest.TestCase):

	def test_number(self):
                print "test_number"
		self.assertEqual(multiply(3,4),12)


if __name__ == '__main__':
	unittest.main()

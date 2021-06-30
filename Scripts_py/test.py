
import unittest

from index import phone_number_code

class TestStringMethods(unittest.TestCase):

    def test_phone_number_code(self):
        Read_data = '9705556816'
        Write_data = '+79705556816'
        phone_number_code()
        self.assertEqual('+7' + Read_data, Write_data)

if __name__ == '__main__':
    unittest.main()
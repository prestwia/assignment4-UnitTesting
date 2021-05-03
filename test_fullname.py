from fullname import fullname
import unittest

f1 = fullname()

class testCalc(unittest.TestCase):
    def test_fullname(self):
        #true test
        self.assertEqual(f1.make_name('John', 'Smith'), 'John Smith')

        #fail test
        self.assertEqual(f1.make_name('John', 'Smith'), 'JohnSmith')

    def test_chars(self):
        #true test
        self.assertEqual(f1.make_name('2lex', 'Jones'), 'Name input cannot have letters or special characters.')

        #fail test
        self.assertEqual(f1.make_name('2lex', 'Jones'), '2lex Jones')

    def test_type(self):
        #true test
        self.assertEqual(f1.make_name(1, 'Smith'), "first or last name input must be string.")

        #fail test
        self.assertEqual(f1.make_name(1, 'Smith'), "1 Smith")


if __name__ == '__main__':
    unittest.main()
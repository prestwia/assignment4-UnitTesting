from average import average
import unittest

a1 = average()

class testCalc(unittest.TestCase):
    def test_avg(self):
        #true test
        self.assertEqual(a1.average_list([1, 2, 3, 4, 5]), 3)
        self.assertEqual(a1.average_list([-3, 2, 3, 4, 5]), 2.2)

        #fail test
        self.assertEqual(a1.average_list([2, 4, 5]), 4)

    def test_empty(self):
        #true test
        self.assertEqual(a1.average_list([]), "List must be populated.")

        #fail test
        self.assertEqual(a1.average_list([-1, 3, 4]), 12)

    def test_type(self):
        self.assertEqual(a1.average_list(['a', 'b', 2]), "List elements must by int or float.")

        #fail test
        self.assertEqual(a1.average_list(['a', 'b', 'c']), "abc")


if __name__ == '__main__':
    unittest.main()
from cube import cube
import unittest

c1 = cube()

class testCalc(unittest.TestCase):
    def test_vol(self):
        #true test
        self.assertEqual(c1.volume(5, 5, 5), 125)

        #fail test
        self.assertEqual(c1.volume(3, 4, 2), 10)

    def test_negative(self):
        #true test
        self.assertEqual(c1.volume(-5, 3, -2), "Inputs must be positive.")

        #fail test
        self.assertEqual(c1.volume(-1, 3, 4), -12)

    def test_type(self):
        self.assertEqual(c1.volume('a', 'b', 2), "Inputs must be type int or float.")

        #fail test
        self.assertEqual(c1.volume('a', 'b', 'c'), "abc")


if __name__ == '__main__':
    unittest.main()
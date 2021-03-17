import unittest

import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)


from src.main import Calc

class Mis_tests(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(Calc().sumar(4, 3), 7)

    def test_resta(self):
        self.assertFalse(Calc().resta(1, 1) == 1)

    def test_multi(self):
        self.assertTrue(Calc().multi(3, 3) == 9)

    if __name__ == '__main__':
        unittest.main()
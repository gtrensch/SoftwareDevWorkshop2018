import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.normalize import *

class TestNormalize(unittest.TestCase):

    def test_value_0(self):
        self.assertEqual(Normalize(0), 0)

    def test_value_1(self):
        self.assertEqual(Normalize(1), 0)

    def test_value_2(self):
        self.assertEqual(Normalize(2), 0)

    def test_value_20(self):
        self.assertEqual(Normalize(20), 0)


def suite():
    suite = unittest.makeSuite(TestNormalize, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()
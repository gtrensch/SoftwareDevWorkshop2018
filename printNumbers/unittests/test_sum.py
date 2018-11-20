import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.sum import *

class TestSum(unittest.TestCase):

    def test_value_1(self):
        self.assertEqual(SumSequence(100), [5050] )


def suite():
    suite = unittest.makeSuite(TestSum, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()
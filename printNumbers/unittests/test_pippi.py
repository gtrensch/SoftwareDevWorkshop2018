# -*- coding: utf-8 -*-
#
# test_pippi.py
#
# This file is part of PrintNumbers.
#
# Copyright (C) 2017 G. Trensch, SLNS, JSC, FZ Jülich
#
# PrintNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# PrintNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PrintNumbers.  If not, see <http://www.gnu.org/licenses/>.

#
# Unit tests: 'fibonacci'.
#

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.pippi import *

class TestPippi(unittest.TestCase):

    def test_value_1_2(self):
        self.assertNotEqual(PippiLangstrumpf(1,2), [3] )

    def test_value_2_1(self):
        self.assertNotEqual(PippiLangstrumpf(1,2), [3] )

    def test_value_0_0(self):
        self.assertEqual(PippiLangstrumpf(0,0), [0])


def suite():
    suite = unittest.makeSuite(TestPippi, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()
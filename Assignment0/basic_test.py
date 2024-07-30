#----------------------------------------------------------------
# File:     basic_test.py
#----------------------------------------------------------------
#
# Author:   Marek Rychlik (rychlik@arizona.edu)
# Date:     Tue Jul 30 09:36:03 2024
# Copying:  (C) Marek Rychlik, 2020. All rights reserved.
# 
#----------------------------------------------------------------
# A basic unit test with the "unittest framework".

import unittest
import solve_quadratic_equation as quadratic

class MyTestCase(unittest.TestCase):
    def test_something(self):
        roots = quadratic.solve_quadratic_equation(1, -1000000.001, 1)
        #print("Testing with unittest, indeed...")
        self.assertAlmostEqual(roots[0], 1000000, places=7, msg = "Not enough places")
        self.assertAlmostEqual(roots[0], 1000000, delta=1e-7, msg = "Delta not met")

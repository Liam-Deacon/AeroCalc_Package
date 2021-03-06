#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test cases for cl module.
Run this script directly to do all the tests.
"""

# Done    1. 29 Jun 2009 - Ran 2to3 tool and fixed errors

import unittest
import sys

from aerocalc import cl


def RE(value, truth):
    """ Return the absolute value of the relative error.
    """

    return abs((value - truth) / truth)


class Test_eas2cl(unittest.TestCase):

    """All truth values hand calculated using a spreadsheet program, using a 
    different approach to correcting for altitude and temperature and using
    ConvertAll for unit conversions.
    """

    def test_01(self):

        Value = cl.eas2cl(
            50,
            1800,
            110,
            weight_units='lb',
            area_units='ft**2',
            speed_units='kt',
            )
        Truth = 1.9333626157
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        Value = cl.eas2cl(
            115,
            700,
            8.5,
            weight_units='kg',
            area_units='m**2',
            speed_units='mph',
            )
        Truth = 0.49889058073
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_cas2cl(unittest.TestCase):

    """All truth values hand calculated using a spreadsheet program, using a 
    different approach to correcting for altitude and temperature and using
    ConvertAll for unit conversions.
    """

    def test_01(self):

        Value = cl.cas2cl(
            200,
            20000,
            2000,
            100,
            weight_units='lb',
            area_units='ft**2',
            speed_units='kt',
            alt_units='ft',
            )
        Truth = 0.15149332672
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        Value = cl.cas2cl(
            80,
            4500,
            700,
            8.5,
            weight_units='kg',
            area_units='m**2',
            speed_units='km/h',
            alt_units='m',
            )
        Truth = 2.6721923079
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_tas2cl(unittest.TestCase):

    """All truth values hand calculated using a spreadsheet program, using a 
    different approach to correcting for altitude and temperature and using
    ConvertAll for unit conversions.
    """

    def test_01(self):

        Value = cl.tas2cl(
            80,
            20000,
            2000,
            100,
            weight_units='lb',
            area_units='ft**2',
            speed_units='kt',
            alt_units='ft',
            )
        Truth = 1.73241190
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        Value = cl.tas2cl(
            80,
            10000,
            2250,
            200,
            200,
            temp_units='K',
            weight_units='kg',
            area_units='m**2',
            speed_units='m/s',
            alt_units='m',
            )
        Truth = 0.07487161
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_cl2eas(unittest.TestCase):

    """All truth values hand calculated using a spreadsheet program, using a 
    different approach to correcting for altitude and temperature and using
    ConvertAll for unit conversions.
    """

    def test_01(self):

        Value = cl.cl2eas(
            0.41956654,
            1000,
            110,
            weight_units='lb',
            area_units='ft**2',
            speed_units='kt',
            )
        Truth = 80
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        Value = cl.cl2eas(
            0.11254822,
            800,
            10,
            weight_units='kg',
            area_units='m**2',
            speed_units='ft/s',
            )
        Truth = 350
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_cl2cas(unittest.TestCase):

    """All truth values hand calculated using a spreadsheet program, using a 
    different approach to correcting for altitude and temperature and using
    ConvertAll for unit conversions.
    """

    def test_01(self):

        Value = cl.cl2cas(
            0.15149332672,
            20000,
            2000,
            100,
            weight_units='lb',
            area_units='ft**2',
            speed_units='kt',
            alt_units='ft',
            )
        Truth = 200
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        Value = cl.cl2cas(
            2.6721923079,
            4500,
            700,
            8.5,
            weight_units='kg',
            area_units='m**2',
            speed_units='km/h',
            alt_units='m',
            )
        Truth = 80
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_cl2tas(unittest.TestCase):

    """All truth values hand calculated using a spreadsheet program, using a 
    different approach to correcting for altitude and temperature and using
    ConvertAll for unit conversions.
    """

    def test_01(self):

        Value = cl.cl2tas(
            1.73241190,
            20000,
            2000,
            100,
            weight_units='lb',
            area_units='ft**2',
            speed_units='kt',
            alt_units='ft',
            )
        Truth = 80
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        Value = cl.cl2tas(
            0.07487161,
            10000,
            2250,
            200,
            200,
            temp_units='K',
            weight_units='kg',
            area_units='m**2',
            speed_units='m/s',
            alt_units='m',
            )
        Truth = 80
        self.assertLessEqual(RE(Value, Truth), 1e-5)

class Test_cl2lift(unittest.TestCase):

    """All truth values hand calculated using a spreadsheet program, using a 
    different approach to correcting for altitude and temperature and using
    ConvertAll for unit conversions.
    """

    def test_01(self):

        Value = cl.cl2lift(
            0.41956654,
            80,
            110,
            lift_units='lb',
            area_units='ft**2',
            speed_units='kt',
            )
        Truth = 1000
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        Value = cl.cl2lift(
            0.11254822,
            350,
            10,
            lift_units='kg',
            area_units='m**2',
            speed_units='ft/s',
            )
        Truth = 800
        self.assertLessEqual(RE(Value, Truth), 1e-5)

# if we run unittest.main(), we get just a single line of output, plus any
# tracebacks from failures.
if __name__ == '__main__':
    unittest.main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# version 0.15, 29 Apr 07

""" Test cases for ssec module.
Run this script directly to do all the tests.
"""
# Done    1. 29 Jun 2009 - Ran 2to3 tool and fixed errors

import unittest
import sys

import aerocalc.ssec as SS


def RE(value, truth):
    """ Returns the absolute value of the relative error.
    """

    return abs((value - truth) / truth)


class Test_gps2tas(unittest.TestCase):

    def test_01(self):

        # three legs, returning TAS only

        Value = SS.gps2tas([178, 185, 188], [178, 82, 355])
        Truth = 183.05
        self.assertLessEqual(RE(Value, Truth), 1e-4)

    def test_02(self):

        # three legs, returning TAS, wind speed and direction

        (TAS, (WS, Dir)) = SS.gps2tas([178, 185, 188], [178, 82, 355],
                1)
        TAS_Truth = 183.05
        WS_Truth = 5.26
        Dir_Truth = 194.5
        self.assertLessEqual(RE(TAS, TAS_Truth), 1e-4)
        self.assertLessEqual(RE(WS, WS_Truth), 1e-3)
        self.assertLessEqual(RE(Dir, Dir_Truth), 1e-4)

        # four legs, returning TAS only

        Value = SS.gps2tas([178, 185, 188, 184], [178, 82, 355, 265])
        Truth = 183.73
        self.assertLessEqual(RE(Value, Truth), 1e-4)

    def test_03(self):

        # three legs, returning TAS, wind speed and direction and heading for each leg

        (TAS, (WS, Dir), (H0, H1, H2)) = SS.gps2tas([178, 185, 188],
                [178, 82, 355], 2)
        TAS_Truth = 183.05
        WS_Truth = 5.26
        Dir_Truth = 194.5
        H0_T = 178.46
        H1_T = 83.52
        H2_T = 354.45
        self.assertLessEqual(RE(TAS, TAS_Truth), 1e-4)
        self.assertLessEqual(RE(WS, WS_Truth), 1e-3)
        self.assertLessEqual(RE(Dir, Dir_Truth), 1e-4)
        self.assertLessEqual(RE(H0, H0_T), 1e-4)
        self.assertLessEqual(RE(H1, H1_T), 1e-4)
        self.assertLessEqual(RE(H2, H2_T), 1e-4)

    def test_04(self):

        # four legs, returning TAS only

        Value = SS.gps2tas([178, 185, 188, 184], [178, 82, 355, 265])
        Truth = 183.73
        self.assertLessEqual(RE(Value, Truth), 1e-4)

    def test_05(self):

        # four legs, returning TAS and standard deviation

        (TAS, SD) = SS.gps2tas([178, 185, 188, 184], [178, 82, 355,
                               265], 1)
        TAS_Truth = 183.73
        SD_Truth = 0.827
        self.assertLessEqual(RE(TAS, TAS_Truth), 1e-4)
        self.assertLessEqual(RE(SD, SD_Truth), 1e-3)

    def test_06(self):

        # four legs, returning TAS, standard deviation and four calculated winds

        (TAS, SD, ((W0, D0), (W1, D1), (W2, D2), (W3, D3))) = \
            SS.gps2tas([178, 185, 188, 184], [178, 82, 355, 265], 2)
        TAS_Truth = 183.73
        SD_Truth = 0.827
        (W0_T, D0_T) = (5.26, 194.52)
        (W1_T, D1_T) = (3.58, 181.52)
        (W2_T, D2_T) = (5.15, 162.7)
        (W3_T, D3_T) = (6.44, 177.95)
        self.assertLessEqual(RE(TAS, TAS_Truth), 1e-4)
        self.assertLessEqual(RE(SD, SD_Truth), 1e-3)
        self.assertLessEqual(RE(D0, D0_T), 1e-4)
        self.assertLessEqual(RE(D1, D1_T), 1e-4)
        self.assertLessEqual(RE(D2, D2_T), 1e-4)
        self.assertLessEqual(RE(D3, D3_T), 1e-4)
        self.assertLessEqual(RE(W0, W0_T), 1e-3)
        self.assertLessEqual(RE(W1, W1_T), 1e-3)
        self.assertLessEqual(RE(W2, W2_T), 1e-3)
        self.assertLessEqual(RE(W3, W3_T), 1e-3)


if __name__ == '__main__':
    unittest.main(verbosity=2)


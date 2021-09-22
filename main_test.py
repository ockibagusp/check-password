#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2021
"""

import unittest


class TestMain(unittest.TestCase):

    def test_main(self):
        # Lists of normal case scenarios.
        listTest = [
            # Case | (Transalator_function, Key Command)
            ("Test1|rpg", 1),
            ("Test2|md5", 2),
            ("Test3|sha1", 3),
            ("Test4|sha224", 4),
            ("Test5|sha256", 5),
            ("Test6|sha384", 6),
            ("Test7|sha512", 7),
            ("Test7|y/n", 0),
            # incorrect
            ("Test8|wrong", -1),
            ("Test9|wrong(2)", 100),
            ("Test10|wrong(3)", "asfff")
        ]

        for (tc, inout) in listTest:
            testcase = str.split(tc, "|")

            if testcase[1] == "rpg":
                out = 1
            elif testcase[1] == "md5":
                out = 2
            elif testcase[1] == "sha1":
                out = 3
            elif testcase[1] == "sha224":
                out = 4
            elif testcase[1] == "sha256":
                out = 5
            elif testcase[1] == "sha384":
                out = 6
            elif testcase[1] == "sha512":
                out = 7
            elif testcase[1] == "y/n":
                out = 0
            elif testcase[1] == "wrong":
                out = -1
            elif testcase[1] == "wrong(2)":
                out = 100
            elif testcase[1] == "wrong(3)":
                out = "asfff"

            self.assertEqual(inout, out)


if __name__ == '__main__':
    unittest.main()

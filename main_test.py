#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2021
"""

import unittest


class TestMain(unittest.TestCase):

    def test_main(self):
        # Lists of normal case scenarios.
        list_test = [
            # ("Case|Main function", "Key Command")
            ("Test1|random_password_generator", 1),
            ("Test2|replace_password", 2),
            ("Test3|md5", 3),
            ("Test4|sha1", 4),
            ("Test5|sha224", 5),
            ("Test6|sha256", 6),
            ("Test7|sha384", 7),
            ("Test8|sha512", 8),
            ("Test9|blake2b", 9),
            ("Test10|blake2s", 10),
            ("Test11|No", 0),
            # incorrect
            ("Test12|wrong", -1),
            ("Test13|wrong(2)", 100),
            ("Test14|wrong(3)", "asfff")
        ]

        for (tc, inout) in list_test:
            testcase = str.split(tc, "|")

            if testcase[1] == "random_password_generator":
                out = 1
            elif testcase[1] == "replace_password":
                out = 2
            elif testcase[1] == "md5":
                out = 3
            elif testcase[1] == "sha1":
                out = 4
            elif testcase[1] == "sha224":
                out = 5
            elif testcase[1] == "sha256":
                out = 6
            elif testcase[1] == "sha384":
                out = 7
            elif testcase[1] == "sha512":
                out = 8
            elif testcase[1] == "blake2b":
                out = 9
            elif testcase[1] == "blake2s":
                out = 10
            elif testcase[1] == "No":
                out = 0
            elif testcase[1] == "wrong":
                out = -1
            elif testcase[1] == "wrong(2)":
                out = 100
            elif testcase[1] == "wrong(3)":
                out = "asfff"

            self.assertEqual(inout, out)

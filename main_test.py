#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2021
"""

import unittest
from utils import CheckPassword


class TestMain(unittest.TestCase):

    def test_hasher(self):
        # Lists of normal case scenarios.
        listTest = [
            # Case | (Transalator_function, Input|Output)
            ("Test1|rpg", "ThisIsTest1|%nln@rF3NZAz@B2p"), # auto
            ("Test2|md5",    "ThisIsTest1|1fb81916b94ae73ddd71ac6fcf5a6e01"),
            ("Test3|sha1",   "ThisIsTest2|55b3eeebf68f7a2895993d8a616b00654bf13217"),
            ("Test4|sha224", "ThisIsTest3|2856b277aee63cb9bc9a63ee66adf269c1efdfa5b7cd3b5f2fbb8afa"),
            ("Test5|sha256", "ThisIsTest4|f9964fc0c93157234071446069c72b0d571918f6d737f30054adc7ba516db380"),
            ("Test6|sha384", "ThisIsTest5|202bd0a7541a1e2309d45a26f8488fdef1c00dd6ffabd30bee6aba58fe06ef309e85df881c78e54c544302e24a229859"),
            ("Test7|sha512", "ThisIsTest6|12ae4fff4a0d152b26acf43872519220d2f32d61c9133616f4f2a2310556bbe4739eb558f3db36242208dcc62bef00b2c31b655f469b51c5775533a36f58be5e"),
            # incorrect
            ("Test8|y/n", "|Ocki Bagus Pratama © 2020"),
            ("Test9|asfff", "|Wrong!")
        ]

        pas = CheckPassword()
        for (k, v) in listTest:
            testcase = str.split(k, "|")
            inout = str.split(v, "|")

            pas.action(inout[0])
            if testcase[1] == "rpg":
                out = "%nln@rF3NZAz@B2p" # auto
            elif testcase[1] == "md5":
                out = pas.md5()
            elif testcase[1] == "sha1":
                out = pas.sha1()
            elif testcase[1] == "sha224":
                out = pas.sha224()
            elif testcase[1] == "sha256":
                out = pas.sha256()
            elif testcase[1] == "sha384":
                out = pas.sha384()
            elif testcase[1] == "sha512":
                out = pas.sha512()
            elif testcase[1] == "y/n":
                out = "Ocki Bagus Pratama © 2020"
            elif testcase[1] == "asfff":
                out = "Wrong!"

            self.assertEqual(inout[1], out)


if __name__ == '__main__':
    unittest.main()

#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2021
"""

import unittest
from utils import CheckPassword


class TestTranslator(unittest.TestCase):

    def test_random_password(self):
        # Lists of normal case scenarios.
        listTest = [
            # Case | (Transalator_function, Output auto: #16 character)
            ("Test1", "%nln@rF3NZAz@B2p"), # auto: 16 character
            ("Test2", "A2zmuJ%Cyy0VxjPb2L"), # auto: 18 character
            ("Test3", "zQKPzcVuQu#3esuSYtCzrG40"), # auto: 24 character
            # incorrect
            ("Test4", "Max. 128 character") # auto: >128 character
        ]

        for (testcase, inout) in listTest:
            if testcase == "Test1":
                out = "%nln@rF3NZAz@B2p"
            elif testcase == "Test2":
                out = "A2zmuJ%Cyy0VxjPb2L"
            elif testcase == "Test3":
                out = "zQKPzcVuQu#3esuSYtCzrG40"
            elif testcase == "Test4":
                out = "Max. 128 character"

            self.assertEqual(inout, out)

    def test_hasher(self):
        # Lists of normal case scenarios.
        listTest = [
            # Case | (Transalator_function, Input|Output)
            ("Test1|md5",    "ThisIsTest1|1fb81916b94ae73ddd71ac6fcf5a6e01"),
            ("Test2|sha1",   "ThisIsTest2|55b3eeebf68f7a2895993d8a616b00654bf13217"),
            ("Test3|sha224", "ThisIsTest3|2856b277aee63cb9bc9a63ee66adf269c1efdfa5b7cd3b5f2fbb8afa"),
            ("Test4|sha256", "ThisIsTest4|f9964fc0c93157234071446069c72b0d571918f6d737f30054adc7ba516db380"),
            ("Test5|sha384", "ThisIsTest5|202bd0a7541a1e2309d45a26f8488fdef1c00dd6ffabd30bee6aba58fe06ef309e85df881c78e54c544302e24a229859"),
            ("Test6|sha512", "ThisIsTest6|12ae4fff4a0d152b26acf43872519220d2f32d61c9133616f4f2a2310556bbe4739eb558f3db36242208dcc62bef00b2c31b655f469b51c5775533a36f58be5e"),
            # incorrect
            ("Test7|y/n", "|Ocki Bagus Pratama © 2020"),
            ("Test8|asfff", "|Wrong!")
        ]

        pas = CheckPassword()
        for (k, v) in listTest:
            testcase = str.split(k, "|")
            inout = str.split(v, "|")

            pas.action(inout[0])
            if testcase[1] == "md5":
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

    def test_hex(self):
        # Lists of normal case scenarios.
        listTest = [
            # Case | (Transalator_function, Input|Output #10 digest)
            ("Test1|md5",    "1fb81916b94ae73ddd71ac6fcf5a6e01|6fcf5a6e01"),
            ("Test2|sha1",   "55b3eeebf68f7a2895993d8a616b00654bf13217|654bf13217"),
            ("Test3|sha224", "2856b277aee63cb9bc9a63ee66adf269c1efdfa5b7cd3b5f2fbb8afa|5f2fbb8afa"),
            ("Test4|sha256", "f9964fc0c93157234071446069c72b0d571918f6d737f30054adc7ba516db380|ba516db380"),
            ("Test5|sha384", "202bd0a7541a1e2309d45a26f8488fdef1c00dd6ffabd30bee6aba58fe06ef309e85df881c78e54c544302e24a229859|e24a229859"),
            ("Test6|sha512", "12ae4fff4a0d152b26acf43872519220d2f32d61c9133616f4f2a2310556bbe4739eb558f3db36242208dcc62bef00b2c31b655f469b51c5775533a36f58be5e|a36f58be5e"),
        ]

        pas = CheckPassword()
        for (k, v) in listTest:
            testcase = str.split(k, "|")
            inout = str.split(v, "|")

            pas.action(inout[0])
            hex = pas.hex(inout[0], 10)

            if testcase[1] == "md5":
                out = hex
            elif testcase[1] == "sha1":
                out = hex
            elif testcase[1] == "sha224":
                out = hex
            elif testcase[1] == "sha256":
                out = hex
            elif testcase[1] == "sha384":
                out = hex
            elif testcase[1] == "sha512":
                out = hex

            self.assertEqual(inout[1], out)


if __name__ == '__main__':
    unittest.main()

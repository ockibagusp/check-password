#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2021
"""

import json
import unittest
from utils import check_password
from sys import version_info


class TestUtils(unittest.TestCase):

    def test_random_password(self):
        # Lists of normal case scenarios.
        list_test = [
            # ("Case", "Output auto")
            ("Test1", "%nln@rF3NZAz@B2p"), # auto: 16 character
            ("Test2", "A2zmuJ%Cyy0VxjPb2L"), # auto: 18 character
            ("Test3", "zQKPzcVuQu#3esuSYtCzrG40"), # auto: 24 character
            # incorrect
            ("Test4", "Max. 128 character") # auto: >128 character
        ]

        for (testcase, inout) in list_test:
            if testcase == "Test1":
                out = "%nln@rF3NZAz@B2p"
            elif testcase == "Test2":
                out = "A2zmuJ%Cyy0VxjPb2L"
            elif testcase == "Test3":
                out = "zQKPzcVuQu#3esuSYtCzrG40"
            elif testcase == "Test4":
                out = "Max. 128 character"

            self.assertEqual(inout, out)

    def test_replace_password(self):
        # replace password: 'a' -> '@', 'B' -> '&'...
        _replaces = '{"a": "@","B": "&","b": "&","C": "<","c": "<","D": "|)","K": "|<","k": "|<","S": "$","s": "$","X": "%","x": "%"," ": "."}'
        data = json.loads(_replaces)
        print(data)
         # Lists of normal case scenarios.
        list_test = [
            # ("Case", "Output")
            ("Test1|ThisIsPassword1", "Thi$I$P@$$word1"),
            ("Test2|ThisIsDolphin2", "Thi$I$|)olphin2"),
            ("Test3|ThisIsCow3", "Thi$I$<ow3"),
            ("Test4|ThisIsSpider4", "Thi$I$$pider4"),            
        ]
        # incorrect

        for (tc, inout) in list_test:
            testcase = str.split(tc, "|")

            s = testcase[1]
            for key, replace in data.items():
                s = s.replace(key, replace)

            self.assertEqual(s, inout)

    def test_hasher(self):
        # Lists of normal case scenarios.
        list_test = [
            # ("Case|Hasher function", "Input|Output")
            ("Test1|md5",       "ThisIsTest1|1fb81916b94ae73ddd71ac6fcf5a6e01"),
            ("Test2|sha1",      "ThisIsTest2|55b3eeebf68f7a2895993d8a616b00654bf13217"),
            ("Test3|sha224",    "ThisIsTest3|2856b277aee63cb9bc9a63ee66adf269c1efdfa5b7cd3b5f2fbb8afa"),
            ("Test4|sha256",    "ThisIsTest4|f9964fc0c93157234071446069c72b0d571918f6d737f30054adc7ba516db380"),
            ("Test5|sha384",    "ThisIsTest5|202bd0a7541a1e2309d45a26f8488fdef1c00dd6ffabd30bee6aba58fe06ef309e85df881c78e54c544302e24a229859"),
            ("Test6|sha512",    "ThisIsTest6|12ae4fff4a0d152b26acf43872519220d2f32d61c9133616f4f2a2310556bbe4739eb558f3db36242208dcc62bef00b2c31b655f469b51c5775533a36f58be5e"),
            ("Test7|No",        "|Ocki Bagus Pratama © 2020"),
            # incorrect
            ("Test8|asfff",     "|Wrong!")
        ]

        # Python 3.6 or later
        if version_info >= (3, 6):
            list_test.append(("Test9|blake2b", "ThisIsTest7|68f750d29e6fb2492b9ded9ae7f2bfc2a24bbc3f2952a69856be4177ae11bd42d55a126eb3ed3a6f89eb05280f52f50b3cb71ae7064cdcc5cf41f624d15ec9a3"))
            list_test.append(("Test10|blake2s", "ThisIsTest8|db81752111c5b1d8ea8c85f032984dffcdb756d5b6d51ac21a4592a2eea9bfeb"))

        pas = check_password()
        for (k, v) in list_test:
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
            elif testcase[1] == "blake2b":
                out = pas.blake2b()
            elif testcase[1] == "blake2s":
                out = pas.blake2s()
            elif testcase[1] == "No":
                out = "Ocki Bagus Pratama © 2020"
            elif testcase[1] == "asfff":
                out = "Wrong!"

            self.assertEqual(inout[1], out)

    def test_hex(self):
        # Lists of normal case scenarios.
        list_test = [
            # ("Case|Hasher function", "Output|10 digest")
            ("Test1|md5",    "e1b849f9631ffc1829b2e31402373e3c|1402373e3c"),
            ("Test2|sha1",   "2b84f621c0fd4ba8bd514c5c43ab9a897c8c014e|897c8c014e"),
            ("Test3|sha224", "5e10e8b7142ca791d7e2c94c6cdb5068a5b7b36513c684588763ca34|588763ca34"),
            ("Test4|sha256", "b9cca56a720f2beee61f2e744ab3d20a95772a4315d18c5eee251a465f078012|465f078012"),
            ("Test5|sha384", "4d5c1ff38f0c3882e91b31962285f803024e9cee8940aa9a1b5936d800058a59221fd31aa9c9d638fd14b28ccecaa78c|8ccecaa78c"),
            ("Test6|sha512", "9ad960eb301b9efd416686821761232e3acaaec24afa7e6e29913990f8e7090f9c74ca4d18a211632a81ac1d92116f26538e655152356972f137ab6229960998|6229960998"),
            ("Test7|blake2b", "04ed9de6f876fdee30be2d19304b32550f9943b750a7e3c2d40cda9b9a287cf7c2ec15ae31d029518deab1f4b9dd78da9e7a7add05e20eb5e909943d2e0b4937|3d2e0b4937"),
            ("Test8|blake2s", "6658043aeb25afe1199b61f1880af58d2eae9211bb94390f72069d5d6ec07181|5d6ec07181"),
        ]

        pas = check_password()
        for (k, v) in list_test:
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
            elif testcase[1] == "blake2b":
                out = hex
            elif testcase[1] == "blake2s":
                out = hex

            self.assertEqual(inout[1], out)

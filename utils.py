#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2020
"""

import string
import random
import hashlib
from sys import version_info


class CekPassword:
    def __init__(self, hasher=False):
        self.cekPython()
        self.hasher = hasher

    # random password generator
    def randomPasswordGenerator(self, generator=16):
        chars = string.ascii_uppercase + string.ascii_lowercase \
            + string.digits + '!#$%?@^' # string.punctuation
        return ''.join(random.choice(chars) for x in range(generator))

    # (?)
    def md5(self):
        _md5 = hashlib.md5()
        _md5.update(self.hasher.encode())
        return _md5.hexdigest()

    # (?)
    def sha1(self):
        _sha1 = hashlib.sha1()
        _sha1.update(self.hasher.encode())
        return _sha1.hexdigest()

    # (?)
    def sha224(self):
        _sha224 = hashlib.sha224()
        _sha224.update(self.hasher.encode())
        return _sha224.hexdigest()

    # (?)
    def sha256(self):
        _sha256 = hashlib.sha256()
        _sha256.update(self.hasher.encode())
        return _sha256.hexdigest()

    # (?)
    def sha384(self):
        _sha384 = hashlib.sha384()
        _sha384.update(self.hasher.encode())
        return _sha384.hexdigest()

    # (?)
    def sha512(self):
        _sha512 = hashlib.sha512()
        _sha512.update(self.hasher.encode())
        return _sha512.hexdigest()

    # (?) Python version 3.6: blake2b() and blake2s()
    def blake2b(self):
        pass

    # (?)
    def blake2s(self):
        pass

    # cek Python
    def cekPython(self):
        # Python 3.x
        if version_info.major == 3:
            if version_info.minor >= 6:
                self.python_version = ">=3.6"
        # Python 2.x
        elif version_info.major == 2:
            self.python_version = "2.x"
            if version_info.minor >= 7:
                # Python 2.7.x or Python 2.6 and earlier exception handling
                self.python_version = ">=2.7"
            raise Exception("Please use Python 3.x or later, not {}.{}."\
                .format(version_info.major, version_info.minor))
        return False

    # print info start
    @ staticmethod
    def print_info(web=False):
        print(
            "Cak Password\n"
            "==================\n"
            "1. random password generator\n"
            "2. md5\n"
            "3. sha1\n"
            "4. sha224\n"
            "5. sha256\n"
            "6. sha384\n"
            "7. sha512\n"
            "0. y/n\n"
        )

    # action (?)
    def action(self, hasher):
        self.hasher = hasher

    # print info end
    @ staticmethod
    def print_info_end(web=False):
        print(
            "\n==================\n"
            "Ocki Bagus Pratama © 2020"
        )

    # hex (?)
    # md5: 1fb81916b94ae73ddd71ac6fcf5a6e01
    #   -> 1fb81916b94ae73ddd71ac6|fcf5a6e01| # 10 digest
    #   -> fcf5a6e01 # 10 digest
    def hex(self, hexdigest, digest=10):
        start = len(hexdigest) - digest
        return hexdigest[start:]

    # run
    def run(self, ops, hasher=False):
        if 1 == ops:
            rpg = self.randomPasswordGenerator()
            return rpg, "random password generator"
        if 2 == ops:
            md5 = self.md5()
            if hasher:
                return md5, self.hex(md5), "md5"
            return md5, self.hex(md5)
        elif 3 == ops:
            sha1 = self.sha1()
            if hasher:
                return sha1, self.hex(sha1), "sha1"
            return sha1, self.hex(sha1)
        elif 4 == ops:
            sha224 = self.sha224()
            if hasher:
                return sha224, self.hex(sha224), "sha224"
            return sha224, self.hex(sha224)
        elif 5 == ops:
            sha256 = self.sha256()
            if hasher:
                return sha256, self.hex(sha256), "sha256"
            return self.sha256(), self.hex(sha256)
        elif 6 == ops:
            sha384 = self.sha384()
            if hasher:
                return sha384, self.hex(sha384()), "sha384"
            return sha384, self.hex(sha384)
        elif 7 == ops:
            sha512 = self.sha512()
            if hasher:
                return sha512, self.hex(sha512), "sha512"
            return sha512, self.hex(sha512)
        elif 0 == ops:
            return self.print_info_end()
        else:
            return "Salah!\n"

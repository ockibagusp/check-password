#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2020
"""

import string
import random
import hashlib
import json
from sys import version_info


class check_password:
    def __init__(self, old_password=None):
        self.check_python()
        self.error = False
        if old_password != None:
            self.old_password = old_password

    # random password generator
    def random_password_generator(self, generator=16):
        chars = string.ascii_uppercase + string.ascii_lowercase \
            + string.digits + '!#$%?@^' # string.punctuation
        return ''.join(random.choice(chars) for x in range(generator))

    # replace password
    def replace_password(self):
        # replaces password JSON file
        _replaces = open('replaces-password.json',)
        data = json.load(_replaces)
        
        for key, replace in data.items():
            self.old_password = self.old_password.replace(key, replace)
        
        _replaces.close()
       
        # byte 'a' => '@'
        # byte 'Cc' => '<', char[0],char[1]{2} => '<' (?)
        new_password = self.old_password
        return new_password

    # md5
    def md5(self):
        _md5 = hashlib.md5()
        _md5.update(self.old_password.encode())
        return _md5.hexdigest()

    # sha1
    def sha1(self):
        _sha1 = hashlib.sha1()
        _sha1.update(self.old_password.encode())
        return _sha1.hexdigest()

    # sha224
    def sha224(self):
        _sha224 = hashlib.sha224()
        _sha224.update(self.old_password.encode())
        return _sha224.hexdigest()

    # sha256
    def sha256(self):
        _sha256 = hashlib.sha256()
        _sha256.update(self.old_password.encode())
        return _sha256.hexdigest()

    # sha384
    def sha384(self):
        _sha384 = hashlib.sha384()
        _sha384.update(self.old_password.encode())
        return _sha384.hexdigest()

    # sha512
    def sha512(self):
        _sha512 = hashlib.sha512()
        _sha512.update(self.old_password.encode())
        return _sha512.hexdigest()

    # Python version 3.6: blake2b() and blake2s()
    def blake2b(self):
        # Python version 3.6
        if version_info >= (3, 6):
            _blake2b = hashlib.blake2b()
            _blake2b.update(self.old_password.encode())
            return _blake2b.hexdigest()
        self.error = True
        return "Please use Python 3.6 or later, not {}.{}."\
                .format(version_info.major, version_info.minor) 

    def blake2s(self):
        # Python version 3.6
        if version_info >= (3, 6):
            _blake2s = hashlib.blake2s()
            _blake2s.update(self.old_password.encode())
            return _blake2s.hexdigest()
        self.error = True
        return "Please use Python 3.6 or later, not {}.{}."\
                .format(version_info.major, version_info.minor)    

    # check Python
    def check_python(self):
        # Python 2.x
        if version_info < (2, 9):
            raise Exception("Please use Python 3.x or later, not {}.{}."\
                .format(version_info.major, version_info.minor))

    # print info start
    @ staticmethod
    def print_info(web=False):
        print(
            "Check Password\n"
            "==================\n"
            "1. random password generator\n"
            "2. replace password\n"
            "3. md5\n"
            "4. sha1\n"
            "5. sha224\n"
            "6. sha256\n"
            "7. sha384\n"
            "8. sha512\n"
            "9. blake2b #Python 3.6 or later\n"
            "10. blake2s #Python 3.6 or later\n"
            "0. No\n"
        )

    # action
    def action(self, old_password):
        self.old_password = old_password

    # print info end
    @ staticmethod
    def print_info_end(web=False):
        print(
            "\n==================\n"
            "Ocki Bagus Pratama © 2020"
        )

    # hex
    # ==============
    # md5: 1fb81916b94ae73ddd71ac6fcf5a6e01
    #   -> 1fb81916b94ae73ddd71ac6|fcf5a6e01| # 10 digest
    #   -> fcf5a6e01 # 10 digest
    #  
    # (?) 10 digest is good. Max. (+10 digest) and Mix. (-10 digest) is no.
    def hex(self, hexdigest, digest=10):
        start = len(hexdigest) - digest
        return hexdigest[start:]

    # run
    def run(self, ops, hasher=False):
        if 1 == ops:
            rpg = self.random_password_generator()
            return rpg, "random password generator"
        if 2 == ops:
            up = self.replace_password()
            return up, "replace password"
        elif 3 == ops:
            md5 = self.md5()
            if hasher:
                return md5, self.hex(md5), "md5"
            return md5, self.hex(md5)
        elif 4 == ops:
            sha1 = self.sha1()
            if hasher:
                return sha1, self.hex(sha1), "sha1"
            return sha1, self.hex(sha1)
        elif 5 == ops:
            sha224 = self.sha224()
            if hasher:
                return sha224, self.hex(sha224), "sha224"
            return sha224, self.hex(sha224)
        elif 6 == ops:
            sha256 = self.sha256()
            if hasher:
                return sha256, self.hex(sha256), "sha256"
            return self.sha256(), self.hex(sha256)
        elif 7 == ops:
            sha384 = self.sha384()
            if hasher:
                return sha384, self.hex(sha384), "sha384"
            return sha384, self.hex(sha384)
        elif 8 == ops:
            sha512 = self.sha512()
            if hasher:
                return sha512, self.hex(sha512), "sha512"
            return sha512, self.hex(sha512)
        elif 9 == ops:
            blake2b = self.blake2b()
            if hasher:
                return blake2b, self.hex(blake2b), "blake2b"
            return blake2b, self.hex(blake2b)
        elif 10 == ops:
            blake2s = self.blake2s()
            if hasher:
                return blake2s, self.hex(blake2s), "blake2s"
            return blake2s, self.hex(blake2s)
        elif 0 == ops:
            return self.print_info_end()
        else:
            return "Wrong!\n"

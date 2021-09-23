#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2020
"""

from utils import CheckPassword

"""
Correct
1. random password generator:   randomPasswordGenerator()
2. md5:                         md5()
3. sha1:                        sha1()
4. sha224:                      sha224()
5. sha256:                      sha256()
6. sha384:                      sha384()
7. sha512:                      sha512()
0. No                           print_info_end()

Incorrect
wrong: -1, 100, and others
wrong: 'asfff' and others
"""

if __name__ == "__main__":
    main = CheckPassword()
    main.print_info()

    number = 1  # randomPasswordGenerator()

    while number:
        try:
            number = int(input("Number (1, 2,..0): "))
            if number > -1 and number != 0 and number <= 7:
                if number != 1:
                    password = input("Password: ")
            elif number != 0: # wrong: -1, 100, and others
                print("Wrong!\n")
                continue
        except ValueError: # wrong: 'asfff' and others
            print("Wrong!\n")
            continue

        if number == 0: # call print_info_end()
            main.run(number)
            break
        elif number == 1: # randomPasswordGenerator()
            _main = main.run(number)
            print("%s -> %s" % (_main[1], _main[0]))
            print("")
            continue

        main.action(password)
        # main.run([md5: 2], [hasher: True] )
        _main = main.run(number, True)
        print("%s -> %s" % (_main[2], _main[0]))
        print("%s -> %s" % (_main[2], _main[1]))
        print("# 10 digest"),
        print("")

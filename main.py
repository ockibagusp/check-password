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
0. no                           print_info_end()

Incorrect
wrong: -1, 100, and others
wrong: 'asfff' and others
"""

if __name__ == "__main__":
    main = CheckPassword()
    main.print_info()

    ops = 1  # randomPasswordGenerator()

    while ops:
        try:
            ops = int(input("Number (1, 2,..0): "))
            if ops != 0 and ops <= 7:
                if ops == 1:
                    print("Password: ")
                else:
                    pas = input("Password: ")
            elif ops != 0: # wrong: -1, 100, and others
                print("Wrong!\n")
                continue
        except ValueError: # wrong: 'asfff' and others
            print("Wrong!\n")
            continue

        if ops == 0: # call print_info_end()
            main.run(ops)
            break
        elif ops == 1: # randomPasswordGenerator()
            m = main.run(ops)
            print("%s -> %s" % (m[1], m[0]))
            continue

        main.action(pas)
        # main.run([md5: 2], [hasher: True] )
        m = main.run(ops, True)
        print("%s -> %s" % (m[2], m[0]))
        print("%s -> %s" % (m[2], m[1]))
        print("# 10 digest"),
        print("")

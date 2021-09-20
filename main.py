#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2020
"""

from utils import CekPassword

if __name__ == "__main__":
    main = CekPassword()
    main.print_info()

    ops = 1  # md5()

    while ops:
        try:
            ops = int(input("Nomer (1, 2,..0): "))
            if ops != 0 and ops <= 6:
                pas = input("Password: ")
            elif ops != 0:
                print("Salah!\n")
                continue
        except ValueError:
            print("Salah!\n")
            continue

        if ops == 0:
            main.run(ops)
            break

        main.action(pas)
        # main.run([md5: 1], [hasher: True] )
        m = main.run(ops, True)
        print("%s -> %s" % (m[2], m[0]))
        print("%s -> %s" % (m[2], m[1]))
        print("# 10 digest"),
        print("")

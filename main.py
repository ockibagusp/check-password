#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama © 2020
"""

from utils import check_password

"""
Correct
1. random password generator:   random_password_generator()
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
    main = check_password()
    main.print_info()

    number = 1  # random_password_generator()

    while number:
        main.error = False
        try:
            number = int(input("Number (1, 2,..0): "))
            if number > -1 and number != 0 and number <= 10:
                if number != 1:
                    old_password = input("Password: ")
            elif number != 0: # wrong: -1, 100, and others
                print("Wrong!\n")
                continue
        except ValueError: # wrong: 'asfff' and others
            print("Wrong!\n")
            continue

        if number == 0: # call print_info_end()
            main.run(number)
            break
         # random_password_generator() or replace_password()
        elif number == 1 or number == 2:
            # replace_password()
            if number == 2:
                main.action(old_password)
            new_password = main.run(number)
            print("%s -> %s" % (new_password[1], new_password[0]))
            print("")
            continue

        main.action(old_password)
        # main.run([md5: 3], [hasher: True] )
        new_password = main.run(number, True)
        # Python version 3.6: blake2b() and blake2s()
        if (number == 9 or number == 10) and main.error == True:
            print("%s -> %s" % (new_password[2], new_password[0]))
            print("")
            continue
        print("%s -> %s" % (new_password[2], new_password[0]))
        print("%s -> %s" % (new_password[2], new_password[1]))
        print("# 10 digest"),
        print("")

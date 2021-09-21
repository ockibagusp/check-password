# Check-Password

Python 2.7 out of support (01 Jan 2020).

Minimum: Python 3.x.

@secgron ini password hacker di Random Password Generator dan Hasher itu susah.

## Random Password Generator

### Pros

- [x] Lowercase (a-z)
- [x] Uppercase (A-Z)
- [x] Numbers (0-9)
- [x] Symbols (&excl;&num;&dollar;&percnt;&quest;&commat;&Hat;)


## Hasher
- [x] md5
- [x] sha1
- [x] sha224
- [x] sha256
- [x] sha384
- [x] sha512
- [ ] blake2b # Python 3.6
- [ ] blake2s # Python 3.6

### Pros

- [x] Lowercase (a-z)
- [ ] Uppercase (A-Z)
- [x] Numbers (0-9)
- [ ] Symbols (&excl;&quot;&num;&dollar;&percnt;&amp;&apos;&lpar;&rpar;&ast;&plus;&comma;&lowbar; ...)


## \$ python main.py

Linux: Fedora 34 Workstation

```
Check Password
==================
1. random password generator
2. md5
3. sha1
4. sha224
5. sha256
6. sha384
7. sha512
0. y/n

Nomer (1, 2,..0): 1
Password: 
random password generator -> %nln@rF3NZAz@B2p
Nomer (1, 2,..0): 2
Password: admin1234
md5 -> c93ccd78b2076528346216b3b2f701e6
md5 -> b3b2f701e6
# 10 digest
```

## Tests

Linux: Python 3.9.7

```
$ python -m unittest -v main_test utils_test
```

Der Schlaganfall 03.10.2018-heute. Dirilis 8 April 2020. Coding ini agak pelupa. Bertahap.

---

Copyright © 2020 by Ocki Bagus Pratama

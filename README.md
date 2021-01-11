# Cek-Password

@secgron, ini password hacker.

- [x] md5
- [x] sha1
- [x] sha224
- [x] sha256
- [x] sha384
- [x] sha512
- [ ] blake2b # Python 3.6
- [ ] blake2s # Python 3.6

Cek

- [x] Lowercase (a-z)
- [x] Numbers (0-9)
- [ ] Uppercase (A-Z)
- [ ] Symbols (! "# \$% & '() \* +, -. / :; <=>? @ [\] ^ \_` {|} ~)

## \$ python main.py

Linux: Fedora 31 Workstation

```
Cak Password
==================
1. md5
2. sha1
3. sha224
4. sha256
5. sha384
6. sha512
0. y/n

Nomer (1, 2,..0): 1
Password: admin1234
md5 -> c93ccd78b2076528346216b3b2f701e6
    -> c93ccd78b2076528346216b|3b2f701e6| # 10 digest
    -> 3b2f701e6 # 10 digest
```

## Tests

Linux: Python 3.7.9

```
$ python -m unittest -v main_test utils_test
```

Der Schlaganfall. Coding lupa, Apr 8 2020, 9 bulan. Tahap-tahap.

---

Copyright © 2020 by Ocki Bagus Pratama

import sys

import passlib.hash


def makepwd(user: str, pwd: str):
    res = passlib.hash.sha512_crypt.hash(pwd, rounds=1024)
    with open('secret/passwd_file', 'a') as f:
        f.write(f'{user}:{res}\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 makepwd.py <user> <password>')
        sys.exit(1)
    makepwd(sys.argv[1], sys.argv[2])

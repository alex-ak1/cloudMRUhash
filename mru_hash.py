import hashlib
import sys


def calcHash(fname):
    h = hashlib.sha1()
    h.update(b'mrCloud')

    total = 0
    with open(fname, "rb") as f:
        data = f.read(1024 * 1024 * 10)
        while data:
            h.update(data)
            total += len(data)

            data = f.read(1024 * 1024 * 10)

    # print( "Len: " + str(l) )
    h.update(str.encode(str(total)))

    return h.digest()


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print('Program generates ETag like cloud.mail.ru service')
        print('  can be useful in verifiying uploaded files')
        print('Usage: python mru_hash.py file_name')
        exit()

    print(calcHash(sys.argv[1]).hex().upper())

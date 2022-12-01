import hashlib

if __name__ == "__main__":
    key = "ckczppom"
    number = 1
    encrypted = hashlib.md5((key + str(number)).encode())
    hexnum = encrypted.hexdigest()
    while hexnum[:5] != "00000":
        number += 1
        encrypted = hashlib.md5((key + str(number)).encode())
        hexnum = encrypted.hexdigest()
    print(f"The key is {number}")
    while hexnum[:6] != "000000":
        number += 1
        encrypted = hashlib.md5((key + str(number)).encode())
        hexnum = encrypted.hexdigest()
    print(f"The second key is {number}")

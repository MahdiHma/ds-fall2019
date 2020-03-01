import struct
from hashlib import sha256


class Blockchain:
    def add_block(self, data):
        n = len(data) + 8
        for i in range(256 ** 4):
            j = sha256(sha256(bytearray.fromhex(data + '{:08X}'.format(i))).digest()).hexdigest()
            if j[-4:] == '0000':
                return '{:08X}'.format(i)


# data = input()
# n = len(data) + 8
# for i in range(256 ** 4):
#     j = sha256(sha256(bytearray.fromhex(data + '{:08X}'.format(i))).digest()).hexdigest()
#     if j[-4:] == '0000':
#         print('{:08X}'.format(i))
#         break

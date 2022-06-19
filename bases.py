import unittest

def dec_to_bin(int32):
    if int32 == 0:
        return "0"

    res = ""
    while (int32 != 0):
        rem = int32 % 2
        res = str(rem) + res
        int32 //= 2
    print(res)
    return res


def bin_to_dec(int8):
    if len(int8) == 0:
        return "0"
    int8 = int(int8)

    curr_int = 0
    res = 0
    while int8 != 0:
        curr_num = int8 % 10
        res += (int8 % 10) * 2 ** curr_int
        curr_int += 1
        int8 //= 10

    print(res)
    return str(res)


def int32_to_ip(int32):
    res = dec_to_bin(int32).zfill(32)
    return bin_to_dec(res[0:8]) + "." + bin_to_dec(res[8:16]) + "." + bin_to_dec(res[16:24]) + "." + bin_to_dec(
        res[24:32])


int32_to_ip(864670712)
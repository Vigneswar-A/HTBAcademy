from Crypto.Util.number import *
from pwn import xor
"""
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0
"""

# def xor(s, n):
#     ascii_num = [ord(c) for c in s]
#     return ''.join(chr(i^13) for i in ascii_num)
# print(xor('label', 13))

"""
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
"""

"""
(F ^ K1 ^ K3 ^ K2) ^ (K2 ^ K3) ^ K1) = F
"""

print(long_to_bytes(0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ^ 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 ^ 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313))

print(xor('opens3same', 'academy'))
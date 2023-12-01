from Crypto.Util.number import *
"""
I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
"""
# input_str = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# key = input_str[0] ^ ord('c')
# print(''.join(chr(c ^ key) for c in input_str))

num = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
flagprefix = bytes('crypto{','utf-8')
print(''.join(chr(num[i]^flagprefix[i]) for i in range(len(flagprefix)))) #myXORke

key = bytes('myXORkey', 'utf-8')

print(''.join(chr(num[i]^key[i%len(key)]) for i in range(len(num))))


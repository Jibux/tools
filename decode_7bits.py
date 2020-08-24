#!/usr/bin/python3


#
# A TOOL TO DECODE GSM 7 BITS
# YOU CAN SEE AT THE BOTTOM OF THIS FILE HOW IT REALLY WORKS
#


import sys


def usage():
    print('Usage: ', sys.argv[0], ' [string_to_decode] (in hexa like "D4F29C0E7A9B41D0FA1C0D4252A950")', sep="")

def gsm7bitdecode(f):
   f = ''.join(["{0:08b}".format(int(f[i:i+2], 16)) for i in range(0, len(f), 2)][::-1])
   return ''.join([chr(int(f[::-1][i:i+7][::-1], 2)) for i in range(0, len(f), 7)])


if len(sys.argv) != 2:
    usage()
    sys.exit(1)

stringToDecode = sys.argv[1]
print(gsm7bitdecode(stringToDecode))


#
# * Intital hexa string: D4 F2 9C 0E 7A 9B 41 D0 FA 1C 0D 42 52 A9 50
# * Intital hexa string (reverse by bytes): 50 A9 52 42 0D 1C FA D0 41 9B 7A 0E 9C F2 D4
# * Get this into groups of 8 bits
# 01010000 10101001 01010010 01000010 00001101 00011100 11111010 11010000 01000001 10011011 01111010 00001110 10011100 11110010 11010100
# * Get this into groups of 7 bits (beginning with the end, bit per bit)
# 0 1010000 1010100 1010100 1001000 0100000 1101000 1110011 1110101 1010000 0100000 1100110 1101111 0100000 1110100 1110011 1100101 1010100
# * Get this into groups 8 bits (reverse by group, 0-padded)
# 01010100 01100101 01110011 01110100 00100000 01101111 01100110 00100000 01010000 01110101 01110011 01101000 00100000 01001000 01010100 01010100 01010000
# Note the 0-padding: 1010100 (end of the 7 bits configuration) -> 01010100 (beginning of the last 8 bits configuration)
# * Get this in ascii = "Test of Push HTTP"
#


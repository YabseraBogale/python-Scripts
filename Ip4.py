"""
ake the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

Examples
2149583361 ==> "128.32.10.1"
32         ==> "0.0.0.32"
0          ==> "0.0.0.0"

The code below need further work
"""
import math
def int32_to_ip(int32):
    # your code here
    if int32 is None:
        return ""
    if int32==0:
        return "0.0.0.0"
    else:
        base=int(math.log(int32,2))
    if int(math.pow(2,base))==int32:
        return f"{int32}.0.0.0"
    bit1=str(bin(int32)).replace('0b','')[0:8]
    bit2=str(bin(int32)).replace('0b','')[8:16]
    bit3=str(bin(int32)).replace('0b','')[16:24]
    bit4=str(bin(int32)).replace('0b','')[24:32]
    lst=[int(bit1,2),int(bit2,2),int(bit3,2),int(bit4,2)]
    ip4=str(lst[0])+"."+str(lst[1])+"."+str(lst[2])+"."+str(lst[3])
    return ip4



print(int32_to_ip(256))

"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
"""
import math
def zeros(n):
    zero=str(math.factorial(n))
    count=0
    i=len(zero)-1
    while 0<=i:
        if zero[i]=="0":
            count+=1
        else:
            break
        i-=1
    return count

print(zeros(5))

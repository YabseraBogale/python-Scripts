
# doesn't work
import math
def exp_sum(n):
    if n == 1: return 1
    elif n == 2: return 2

    repeats = range(2, n+1)
    possible_numbers = []
    
    for repeat in repeats:
        possible_numbers += math.prod(list(range(1, n)))
    
    result = []
    for x in possible_numbers:
        x = sorted(x)
        if sum(x) == n and x not in result:
            result.append(x)
    
    return len(result)+1
print(exp_sum(100))

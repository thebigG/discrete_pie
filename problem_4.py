import itertools
import math
def count_mod_in_set(n, m):
    set = itertools.product(range(m), repeat = n)
    count = 0
    set_count = 0
    for sub_set in set:
        set_count +=1
        # print(sub_set)
        if((int(math.fsum(sub_set)) % m) == 1 ):
            # print("mod = 1 for:", sub_set)
            count += 1
    print("set_count:", set_count)
    return count




def find_factor(n):
    factor_values = []
    for i in range(1, n +1):
        if n % i == 0:
            factor_values.append(i)
    return factor_values

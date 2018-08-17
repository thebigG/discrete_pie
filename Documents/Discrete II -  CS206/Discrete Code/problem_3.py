import itertools


def is_before_greater(list, i):
    pivot = list[i]
    is_greater = True
    for item in range(i):
        if list[item] < pivot:
            is_greater = False
            break
    return is_greater

def is_before_less(list, i):
    pivot = list[i]
    is_less = True
    for item in range(i):
        if list[item] > pivot:
            is_less = False
            break
    return is_less



def is_zig_zag(nums):
    zig_zag  =True
    for num in range(1,len(nums)):
        if not(is_before_less(nums, num) or is_before_greater(nums, num)):
            zig_zag = False
            break
    return zig_zag



def zig_zag_count(num):
    nums = range(1, num +1)
    nums_permutations = itertools.permutations(nums, len(nums))
    count  = 0
    times_called  = 0
    for permutation in nums_permutations:
        if is_zig_zag(permutation):
            count += 1
    # print("times called:", times_called)
    return count

def zig_zag_permutations(num):
    nums = range(1, num +1)
    nums_permutations = itertools.permutations(nums, len(nums))
    count  = 0
    times_called  = 0
    zig_zags  = []
    for permutation in nums_permutations:
        if is_zig_zag(permutation):
            zig_zags.append(permutation)
    # print("times called:", times_called)
    return zig_zags

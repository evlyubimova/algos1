"""
q = 10
max_val = 1000
nums = [1, 56, 23, 45, 88, 14, 76, 3, 65, 14]
"""

"""
Time
t(n) = 2t(n/2) +cn
"""


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        mid = len(numbers)//2
        left = merge_sort(numbers[:mid])
        right = merge_sort(numbers[mid:])
        return merge(left, right)


def merge( lft, rgt):
    result = []
    while len(lft)>0 and len(rgt)>0:
        if lft[0] >= rgt[0]:
            result.append(rgt[0])
            rgt.pop(0)
        else:
            result.append(lft[0])
            lft.pop(0)
    if len(lft) >0:
        result += lft
    if len(rgt) >0:
        result += rgt
    return result

q = int(input())

nums = [int(x) for x in input().split()]
print(*merge_sort(nums))
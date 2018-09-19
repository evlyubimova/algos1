import random
"""
q = 10
nums = [1, 56, 23, 45, 88, 14, 76, 3, 65, 10]
"""
q = int(input())
nums = [int(x) for x in input().split()]


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        sep = random.choice(nums)
        sm = []
        eq = []
        bi = []
        for n in numbers:
            if n > sep:
                bi.append(n)
            elif n ==sep:
                eq.append(n)
            else:
                sm.append(n)
        return quick_sort(sm) + eq + quick_sort(bi)


print(*quick_sort(nums))


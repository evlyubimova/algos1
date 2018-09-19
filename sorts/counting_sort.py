
q = 10
max_val = 1000
nums = [1, 56, 23, 45, 88, 14, 76, 3, 65, 14]
"""
q = int(input())
max_val = int(input())
nums = [int(x) for x in input().split()]
"""


def counting_sort(numbers, max_value):
    counts = [0] * max_value
    for i in range(len(numbers)):
        counts[numbers[i]] += 1

    result = []
    for j in range(len(counts)):
        for k in range(counts[j]):
            result.append(j)
    return result


print(*counting_sort(nums, max_val))

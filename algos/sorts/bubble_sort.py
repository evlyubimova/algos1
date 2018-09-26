"""
n = 5
nums = [3,2,9,6,5]
"""
n= int(input())
nums = [int(x) for x in input().split()]

print(*nums)
for i in range(n - 2):
    for j in range(n - i-1):
        if nums[j]  >  nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
    print( i, " ", *nums)
print(*nums)

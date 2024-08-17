# def removeElement(nums, val):
#     for i in nums:
#         if i == val:
#             nums.remove(i)
#         else:
#             continue
#     return nums
#
#
# a = removeElement(nums=[1, 2, 2, 3, 2, 4], val=2)
# print(a)

def removeElement(nums, val):
    lst = []
    for i in range(len(nums)):
        if nums[i] == val:
            lst.append(i)
    lst.reverse()
    for i in lst:
        nums.pop(i)
    return len(nums)


a = removeElement(nums=[1, 2, 2, 3, 2, 4], val=2)
print(a)

# def removeElement(nums, val):
#     i = 0
#     for x in nums:
#         if x != val:
#             nums[i] = x
#             i += 1
#     return i
#
#
# a = removeElement(nums=[1, 2, 2, 2, 2, 4], val=2)
# print(a)

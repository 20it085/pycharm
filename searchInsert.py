# def searchInsert(nums, target):
#     for i in nums:
#         if nums[i] == target:
#             a = nums.index(i + 1)
#             print(a)
#         elif nums[i] < target < nums[i + 1]:
#             a = nums.index(i + 1)
#             print(a)
#     else:
#         print(len(nums)+1)
#
#
# searchInsert(nums=[1, 2, 3, 5], target=2)


# def searchInsert(nums, target):
#     nums.append(target)
#     return sorted(nums).index(target)
#
#
# a = searchInsert(nums=[1, 2, 3, 4], target=5)
# print(a)


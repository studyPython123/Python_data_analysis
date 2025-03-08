def merge(nums1, nums2):
    nums = []
    for i in nums1:
        if i != 0:
            nums.append(i)
    for i in nums2:
        if i != 0:
            nums.append(i)
    nums.sort()
    return nums
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(nums1, nums2))
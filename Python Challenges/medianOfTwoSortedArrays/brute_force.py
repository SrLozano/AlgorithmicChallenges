class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mixed_nums = sorted(nums1 + nums2)
        # odd case
        if len(mixed_nums) % 2 == 1:
            return mixed_nums[len(mixed_nums) // 2]
        # even case
        else:
            mid1 = mixed_nums[(len(mixed_nums) // 2) - 1]
            mid2 = mixed_nums[(len(mixed_nums) // 2)]
            return (mid1 + mid2)/2
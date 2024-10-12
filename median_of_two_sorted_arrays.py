from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            # Số lượng phần tử lẻ
            median = nums[length // 2]
        else:
            # Số lượng phần tử chẵn
            median = (nums[length // 2 - 1] + nums[length // 2]) / 2.0
        return median


solution = Solution()

print(solution.findMedianSortedArrays([1, 2, 3, 4, 5],[100]))
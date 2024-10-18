class Solution(object):
    def maxArea(self, height):
        
        result = 0

        # Solution 1
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                area = min(height[left],height[right]) * (right - left)
                result = max(result,area)

        # Solution 2
        # left = 0
        # right = len(height) - 1

        # while left < right:
        #     area = min(height[left],height[right]) * (right - left)
        #     result = max(result,area)

        #     if height[left] <= height[right]:
        #         left += 1
        #     else:
        #         right -= 1
            

        return result

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
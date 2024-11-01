class Solution(object):
    def threeSumClosest(self, nums, target):
        result = None
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                else:
                    if result is None or abs(target - total) < abs(target - result):
                        result = total

                    if total < target:
                        left += 1
                    else:
                        right -= 1

        print(result)
        return result


solution = Solution()
print(solution.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))  # Trả về 2

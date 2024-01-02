class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i in range(len(nums)):
            sec_value = target - nums[i]
            if sec_value in map:
                return [i, map[sec_value]]
            map[nums[i]] = i


nums = [3,2,3]
target = 6

s = Solution()
print(s.twoSum(nums, target))

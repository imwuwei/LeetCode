#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i

# @lc code=end


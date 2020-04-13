#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # import os
        # return os.path.commonprefix(strs)
        if len(strs) == 0:
            return ""
        s = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(s) !=0:
                s = s[:-1]
        return s
    
# @lc code=end


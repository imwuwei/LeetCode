#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.71%)
# Likes:    3456
# Dislikes: 0
# Total Accepted:    427.1K
# Total Submissions: 1.3M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}    # 存放字符最后出现的位置索引
        ans = 0         # 最长无重复字符串的长度
        i = -1          # 字符最后出现的位置索引，初始为-1
        for index, num in enumerate(s):
            if num in hashmap:
                # 获得字符最后出现的位置索引赋给i
                i = max(hashmap[num], i)
            # index - i 两个相同字符串的索引相减，得出不重复字符串的长度
            # 再调用max()函数，与ans比较获取最大的一个赋给ans
            ans = max(ans, index - i) 
            hashmap[num] = index
        return ans


# @lc code=end


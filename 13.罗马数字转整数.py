#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# 解析，先建立字典dic，然后遍历字符串s，
# 如果该字符小于它右边的字符，sum就减掉dic[num]
# 如果该字符大于它右边的字符，sum就加上dic[num]
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for index, num in enumerate(s):
            if index + 1 >= len(s):
                sum += dic[num]
                return sum
            elif dic[num] < dic[s[index+1]]:
                sum -= dic[num]
            else:
                sum += dic[num]

# @lc code=end


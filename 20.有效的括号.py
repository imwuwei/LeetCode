#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
# 
# 思路：
# 利用栈的思想，遍历字符串，将左括号压入栈中，
# 如果遇到右括号就删除栈顶的元素
# 最后判断栈是否为空就行
# 理想情况下字符串是有效的，即括号都能匹配
# 一些情况会报异常，即字符串无效

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "}":"{", "]":"["}
        arr = []
        try:
            for i in s:
                if i in mapping and mapping[i] == arr[-1]:
                    arr.pop()
                else:
                    arr.append(i)
            if not arr:
                return True
            else:
                return False
        except:
            return False
# @lc code=end


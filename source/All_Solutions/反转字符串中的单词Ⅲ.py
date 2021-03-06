# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
# 示例 1:
#
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"
# 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        i,j = 0,0
        while i < len(s):反转反转
            if s[i] == ' ':
                res += s[j:i][::-1] + ' '
                j = i+1
            i += 1
        return res + s[j:i][::-1]
# -*- coding: utf-8 -*-
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        tran = [0] * len(s)
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    tran[i] = 1
                else:
                    stack.pop()
        for i in stack:
            tran[i] = 1
        num = 0
        n = 0
        for flag in tran:
            if flag:
                n = 0
                continue
            n += 1
            num = max(num,n)
        return num
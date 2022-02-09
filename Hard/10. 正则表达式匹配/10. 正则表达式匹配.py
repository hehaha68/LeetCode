# -*- coding: utf-8 -*-
""" 
@Time    : 2022/2/9 23:29
@Author  : 和泳毅
@FileName: 10. 正则表达式匹配.py
@SoftWare: PyCharm
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # NFA
        nfa = [[]]
        for pi in range(len(p)):
            if pi < len(p) - 1 and p[pi + 1] == '*':
                nfa[-1].append([p[pi], len(nfa) - 1])
            elif p[pi] != '*':
                nfa[-1].append([p[pi], len(nfa)])
                nfa.append([])

        state = {(0, 0)}  # 初始化状态集合
        for char in s:
            step = set()  # 空集合
            for state0, state1 in state:
                if state0 >= len(nfa):
                    continue
                for j, [c, n] in enumerate(nfa[state0][state1:]):
                    if c == '.' or c == char:
                        if n == state0:
                            step.add((n, j + state1))
                        else:
                            step.add((n, 0))
            if len(step) == 0:
                return False
            state = step
            del step
        for state0, state1 in state:
            if state0 == len(nfa) - 1:
                return True
        return False
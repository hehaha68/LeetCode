# -*- coding: utf-8 -*-
from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        result = []
        len_s = len(s)
        len_word = len(words[0])
        len_words = len(words)
        k = len_word * len_words
        # words中每个单词当且仅当匹配一次，用于比对是否符合题设
        word_num = Counter(words)
        # 单词长度相同，从不同的起始点开始滑动窗口，可以将步长设置为单词长度
        for start in range(len_word):
            i, j = start, 0
            match_num = Counter()
            # 注意边界范围
            while i < len_s - k + 1:
                # 小窗口需且只需匹配len_words个单词
                while j < len_words:
                    m = i + j * len_word
                    word = s[m:m + len_word]
                    # 如果某小窗口内单词不在words内 或者 Hash表该单词计数值超过应有值 则可以退出小窗口的滑动
                    if (word not in words) or (match_num[word] >= word_num[word]):
                        break
                    # 使用Hash表对小窗口内单词计数
                    match_num[word] += 1
                    j += 1
                # 如果符合题设，将位置存储
                if match_num == word_num:
                   result.append(i)
                # 最后标记的word在words中，则可以利用已有信息进行优化，即小窗口匹配的所有word一定在words中
                if word in words:
                    # 窗口移动到小窗口匹配的第一个word后，相应的Hash计数减一，下次小窗口匹配只向后移动一次
                    match_num[s[i:i + len_word]] -= 1
                    i += len_word
                    j -= 1
                else:
                    # 否则表示下一趟小窗口匹配也会遇到该word不在words中，所以移动窗口到该word之后，小窗口重置
                    i, j = m + len_word, 0
                    match_num.clear()
        return result

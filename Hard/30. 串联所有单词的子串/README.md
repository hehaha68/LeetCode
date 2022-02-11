#### [30. 串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)

给定一个字符串 s 和一些长度相同的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

-----------

想到使用滑动窗口来解决匹配类问题是不难的，但此题包含一些数据量略大的测试案例，所以如何优化是关键。

首次尝试暴力解法看看能不能蒙混过关，使用递归来判断是否将words中的所有单词当且仅当匹配一遍：

```python
def match(self, s, words, len_word):
    if len(words) == 0:
       return True
    if s[:len_word] in words:
        sub_words = list(words)
        sub_words.remove(s[:len_word])
        return self.match(s[len_word:], sub_words, len_word)
    return False
```

但是样例174超过最大递归深度。。。。。。

于是开始优化程序，既然开始优化就干脆优化得彻底一点。首先计算之后会重复使用的数值：

```python
result = []
len_s = len(s)
len_word = len(words[0])
len_words = len(words)
k = len_word * len_words
```

由单词长度相同这一性质可以启发出步长规律。通过不同的起始位置，可以将步长设置为单词长度而不是每次移动一个字符，这样依然可以囊括所有可能，并且有利于对一些特殊情况优化。

例如：s = "barfoothefoobarman"，words = ["foo","bar"]

1. [bar] [foo] [the] [foo] [bar] [man]
2. b [arf] [oot] [hef] [oob] [arm] an
3. ba [rfo] [oth] [efo] [oba] [rma] n

又注意到子串要与words中的单词完全匹配，这里使用Hash表来计数处理，子串中每个小窗口囊括的单词出现次数，一定要对于words中单词出现次数，这也符合题设不计单词次序的要求。

```python
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
	    "....."
```

接着可以对一些特殊情况进行优化，思考KMP算法中对已有信息的利用，即能否使用已经“访问”的单词信息来优化窗口的移动：

- 最后标记的word在words中，表示上一趟匹配符合题设或者遇到match_num[word] > word_num[word]的情况：

  1. 【[bar] [foo]】 the foo bar man	→	bar 【[foo] [the]】 foo bar man
  2. 【[bar] [bar]】 the foo bar man	→	bar 【[bar] [the]】 foo bar man

- 最后标记的word不在words中，蕴含着下一趟匹配也会遇到这个单词：

  bar 【[foo] [the]】 foo bar man	→	bar foo the 【[foo] [bar]】 man

```python
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
```

最终将时间从2000ms逐渐降到60ms。

执行用时：60 ms, 在所有 Python 提交中击败了94.42%的用户

内存消耗：13.4 MB, 在所有 Python 提交中击败了91.08%的用户

通过测试用例：176 / 176
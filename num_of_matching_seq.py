# given string s and an array of string words, return number of words[i] that is a subsequence of s
# new string generated from og string with some char deleted, relative order not changed
from collections import defaultdict

def subsequences(s, words):
    waiting = [[] for _ in range(26)]
    ans = 0
    for word in words:
        it = iter(word)
        waiting[ord(next(it)) - ord("a")].append(it)
    for character in s:
        letter_ind = ord(character) - ord("a")
        old_bucket = waiting[letter_ind]
        waiting [letter_ind] = []
        while old_bucket:
            it = old_bucket.pop()
            nxt = next(it, None)
            if nxt:
                waiting[ord(nxt) - ord("a")].append(it)
            else:
                ans += 1
    return ans

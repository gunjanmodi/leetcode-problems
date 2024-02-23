from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        result = ""
        d = Counter(t)
        total_chars = len(d)
        i, min_length_string, start, end = 0, float('inf'), 0, float('inf')

        for j in range(len(s)):
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    total_chars -= 1

            while total_chars == 0:
                if j - i + 1 <= min_length_string:
                    min_length_string = j - i + 1
                    start, end = i, j

                if s[i] in d:
                    d[s[i]] += 1
                    if d[s[i]] == 1:
                        total_chars += 1
                i += 1

        if end == float('inf'):
            return ""

        return s[start:end + 1]

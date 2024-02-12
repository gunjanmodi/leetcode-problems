class Solution:
    def minFlips(self, s: str) -> int:
        option1, option2, k = ['0'], ['1'], len(s)
        get_next = {'0': '1', '1': '0'}
        result = float('inf')
        s += s

        for i in range(1, len(s)):
            option1.append(get_next[option1[-1]])
            option2.append(get_next[option2[-1]])

        valid1, valid2 = ''.join(option1), ''.join(option2)
        diff1, diff2 = 0, 0
        i = 0
        for j in range(len(s)):
            if s[j] != valid1[j]:
                diff1 += 1
            if s[j] != valid2[j]:
                diff2 += 1

            if j - i + 1 >= k:
                result = min(result, diff1, diff2)
                if s[i] != valid1[i]:
                    diff1 -= 1
                if s[i] != valid2[i]:
                    diff2 -= 1
                i += 1
            
        return result

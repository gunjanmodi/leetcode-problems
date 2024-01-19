class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < 2 ** k:
            return False
        i, string_set = 0, set()
        for j in range(len(s)):
            if j - i + 1 == k:
                ss = s[i:j + 1]
                string_set.add(ss)
                i += 1
        return len(string_set) == 2 ** k  

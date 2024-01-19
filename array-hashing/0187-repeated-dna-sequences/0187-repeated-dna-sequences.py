from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i, d = 0, defaultdict(int)
        
        for j in range(len(s)):
            if j - i + 1 == 10:
                ss = s[i:j+1]
                d[ss] += 1
                i += 1

        return [k for k, v in d.items() if v > 1]
        
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        i, total_chars = 0, len(d)

        for j in range(len(s2)):

            while j - i + 1 > len(s1):
                if s2[i] in d:
                    d[s2[i]] += 1
                    if d[s2[i]] == 1:
                        total_chars += 1
                i += 1

            if s2[j] in d:
                d[s2[j]] -= 1
                if d[s2[j]] == 0:
                    total_chars -= 1

                if total_chars == 0:
                    return True
        return False

            
            

                

        
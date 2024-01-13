from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        total = len(counter)
        result, i, k = [], 0, len(p)
        
        for j in range(len(s)):
            if s[j] in counter:
                counter[s[j]] -= 1

                if counter[s[j]] == 0:
                    total -= 1

                if total == 0:
                    result.append(i)

            if j - i + 1 == k:
                if s[i] in counter:
                    counter[s[i]] += 1

                    if counter[s[i]] == 1:
                        total += 1
                i += 1

        return result

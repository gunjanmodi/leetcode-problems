class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, result, count = 0, 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for j in range(len(s)):

            while j - i + 1 > k:
                if s[i] in vowels:
                    count -= 1
                i += 1

            if s[j] in vowels:
                count += 1
                result = max(result, count)

        return result

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, largest_str, hs = 0, 0, set()

        for j in range(len(s)):

            while s[j] in hs:
                hs.remove(s[i])
                i += 1

            hs.add(s[j])
            largest_str = max(largest_str, len(hs))

        return largest_str
        
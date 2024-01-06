class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        c = 0

        while c < len(first):
            if first[c] == last[c]:
                c += 1
            else:
                break

return "" if c == 0 else first[:c]

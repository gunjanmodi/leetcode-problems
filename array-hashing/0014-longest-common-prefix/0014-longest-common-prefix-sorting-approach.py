class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and first[i] == last[i]:
            i += 1
                
        return "" if i == 0 else first[:i]
        

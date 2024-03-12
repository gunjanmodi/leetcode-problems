class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        char_list_s = list(s)
        
        def is_valid(k):
            for i in range(k + 1):
                char_list_s[removable[i]] = '#'
            
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if char_list_s[i] == '#':
                    i += 1
                elif char_list_s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1

            if j == len(p):
                return True
            
            for i in range(k + 1):
                char_list_s[removable[i]] = s[removable[i]]
            
            return False
            
        max_removable = -1
        left, right = 0, len(removable) - 1

        while left <= right:
            mid = (left + right) >> 1
            if is_valid(mid):
                max_removable = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return max_removable + 1

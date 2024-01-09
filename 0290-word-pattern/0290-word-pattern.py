class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_array = s.split(' ')

        if len(pattern) != len(s_array):
            return False
        
        p_dict, s_dict = {}, {}
        for i in range(len(pattern)):
            if pattern[i] in p_dict or s_array[i] in s_dict:
                if p_dict.get(pattern[i]) != s_dict.get(s_array[i]):
                    return False
        
            p_dict[pattern[i]] = i
            s_dict[s_array[i]] = i

        return True



        
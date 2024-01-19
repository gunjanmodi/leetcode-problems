class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_ch, t_ch = s[i], t[i]

            if (s_ch in s_dict and s_dict[s_ch] != t_ch) or (t_ch in t_dict and t_dict[t_ch] != s_ch):
                return False

            s_dict[s_ch] = t_ch
            t_dict[t_ch] = s_ch
            
        return True
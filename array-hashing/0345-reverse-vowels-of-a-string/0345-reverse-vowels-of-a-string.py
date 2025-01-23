class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        s_list = [c for c in s]
        
        while i < j:
            
            while i < j and s_list[i] not in vowels:
                i += 1
            
            while i < j and s_list[j] not in vowels:
                j -= 1

            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1

        return ''.join(s_list)
        
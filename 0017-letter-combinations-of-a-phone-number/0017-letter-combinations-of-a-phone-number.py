class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result

        ref = {'2':['a','b','c'], '3': ['d','e','f'], '4': ['g', 'h', 'i'], '5': ['j','k','l'],
         '6': ['m','n','o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w','x','y','z']
        }

        def backtrack(i, combination):
            if len(combination) == len(digits):
                result.append(''.join(combination[:]))
                return
            
            while i < len(digits):
                for c in ref[digits[i]]:
                    combination.append(c)
                    backtrack(i + 1, combination)
                    combination.pop()
                i += 1

        backtrack(0, [])

        return result

            




        
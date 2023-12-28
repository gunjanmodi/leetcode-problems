class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(num, combination):
            if len(combination) == k:
                result.append(combination[:])
                return
                
            if num > n:
                return
            
            # take
            combination.append(num)
            backtrack(num + 1, combination)

            # not take
            combination.pop()
            backtrack(num + 1, combination)
        
        backtrack(1, [])

        return result
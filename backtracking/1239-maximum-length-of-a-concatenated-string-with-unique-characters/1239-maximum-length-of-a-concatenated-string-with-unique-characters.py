class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        max_count = [0]

        def is_valid_choice(s, combination):
            if len(s) != len(set(s)):
                return False

            for c in s:
                if c in combination:
                    return False

            return True

        def backtrack(i, combination):
            max_count[0] = max(max_count[0], len(combination))

            if i == len(arr):
                return

            for j in range(i, n):
                temp = arr[j]

                if is_valid_choice(temp, combination):
                    for c in temp:
                        combination.add(c)
                        
                    backtrack(j+1, combination)
                    
                    for c in temp:
                        combination.remove(c)


        backtrack(0, set())
        return max_count[0]

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)

        def backtrack(i, combination):
            if i == n:
                temp = ''.join(combination)
                if temp not in nums_set:
                    return temp
                else:
                    return ''

            combination.append('0')
            answer_zero = backtrack(i+1, combination)
            if answer_zero:
                return answer_zero
            combination.pop()

            combination.append('1')
            answer_one = backtrack(i+1, combination)
            if answer_one:
                return answer_one
            combination.pop()

        return backtrack(0, [])






        
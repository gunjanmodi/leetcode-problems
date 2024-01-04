class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        desired_sum = total // 4
        matchsticks.sort(reverse=True)

        square = [0 for _ in range(4)]

        def helper(i):
            if i == n:
                for edge in square:
                    if edge != desired_sum:
                        return False
                return True

            for j in range(4):
                if square[j] + matchsticks[i] <= desired_sum:
                    square[j] += matchsticks[i]
                    if helper(i + 1):
                        return True
                    square[j] -= matchsticks[i]
                    if square[j] == 0:
                        break
            return False

        return helper(0)
      
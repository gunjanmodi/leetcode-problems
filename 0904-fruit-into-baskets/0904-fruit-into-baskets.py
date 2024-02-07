class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, result, d = 0, 0, {}

        for j in range(len(fruits)):

            d[fruits[j]] = d.get(fruits[j], 0) + 1
            
            while len(d) > 2:
                d[fruits[i]] -= 1

                if d[fruits[i]] == 0:
                    d.pop(fruits[i])

                i += 1

            result = max(result, j - i + 1)

        return result


        
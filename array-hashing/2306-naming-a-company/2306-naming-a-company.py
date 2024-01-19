class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d = collections.defaultdict(set)
        for idea in ideas:
            ch1, others = idea[0], idea[1:]
            d[ch1].add(others)
        
        suffix = list(d.values())
        count = 0
        for i in range(len(suffix)):
            for j in range(i + 1, len(suffix)):
                count1 = len(suffix[i] - suffix[j])
                count2 = len(suffix[j] - suffix[i])
                count += (2 * count1 * count2)
                
        return count

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d = collections.defaultdict(list)
        for w, h in rectangles:
            d[w/h].append([w, h])

        result = 0
        for k in d:
            n = len(d[k])
            result += (n * (n-1) // 2)
        return result
        
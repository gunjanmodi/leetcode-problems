from collections import Counter
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        d = Counter(customers)
        min_penalty, min_index, prev_penalty = float('inf'), 0, 0

        for i, ch in enumerate(customers):
            if ch == 'Y':
                penalty = d['Y'] + prev_penalty
                d['Y'] -= 1
            else:
                penalty = d['Y'] + prev_penalty
                prev_penalty += 1
            
            if penalty < min_penalty:
                min_penalty = penalty
                min_index = i

        if prev_penalty < min_penalty:
            return len(customers)
            
        return min_index
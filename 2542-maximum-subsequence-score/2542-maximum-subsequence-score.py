from heapq import heappop, heappush


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums2, nums1))
        pairs.sort(key=lambda x:x[0], reverse = True)
        
        min_heap, current_sum, answer = [], 0, 0
        
        for i in range(k-1):
            heappush(min_heap, pairs[i][1])
            current_sum += pairs[i][1]

        for i in range(k-1, len(nums1)):
            heappush(min_heap, pairs[i][1])
            current_sum += pairs[i][1]
            
            answer = max(answer, pairs[i][0] * current_sum)
            
            min_num = heappop(min_heap)
            current_sum -= min_num
            
        return answer

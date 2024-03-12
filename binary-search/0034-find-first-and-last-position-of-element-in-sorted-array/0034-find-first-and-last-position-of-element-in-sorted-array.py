class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [float('inf'), float('-inf')]
        def binary_search(left, right):
           
            while left <= right:
                mid = (left + right) >> 1
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                elif target == nums[mid]:
                    answer[0] = min(answer[0], mid)
                    answer[1] = max(answer[1], mid)
                    binary_search(left, mid - 1)
                    binary_search(mid + 1, right)
                    break 

            return -1

        binary_search(0, len(nums) - 1)

        if answer[0] == float('inf'):
            answer[0] = -1
        if answer[1] == float('-inf'):
            answer[1] = -1
        return answer
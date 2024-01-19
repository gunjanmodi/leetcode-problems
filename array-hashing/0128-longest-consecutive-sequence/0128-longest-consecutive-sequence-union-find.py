class UnionFind:
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(self.size)]
        self.rank = [1 for _ in range(self.size)]

    def find(self, x):
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            self.parent[parent_x] = parent_y
            self.rank[parent_y] += self.rank[parent_x]
            self.rank[parent_x] = 0

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(len(nums))
        value_to_idx = {}

        for i in range(len(nums)):
            if nums[i] in value_to_idx:
                continue
            if nums[i] - 1 in value_to_idx:
                uf.union(i, value_to_idx[nums[i] - 1])

            if nums[i] + 1 in value_to_idx:
                uf.union(i, value_to_idx[nums[i] + 1])

            value_to_idx[nums[i]] = i

        return max(uf.rank) if uf.rank else 0

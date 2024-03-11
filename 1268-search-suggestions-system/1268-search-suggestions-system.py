class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = [[] for _ in range(len(searchWord))]
        products.sort()

        left, right = 0, len(products) - 1

        for i in range(len(searchWord)):
            c = searchWord[i]

            while left <= right and (len(products[left]) <= i or products[left][i] != c):
                left += 1
            
            while left <= right and (len(products[right]) <= i or products[right][i] != c):
                right -= 1

            remaining = right - left + 1
            for j in range(min(3, remaining)):
                result[i].append(products[left + j])
        
        return result

class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.current.next = node
        node.prev = self.current
        self.current = node

    def back(self, steps: int) -> str:
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val
            
    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
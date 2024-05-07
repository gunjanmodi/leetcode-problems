class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        node = ListNode(homepage)
        self.head = node
        self.tail = node
        self.current = node
        
    def visit(self, url: str) -> None:
        node = ListNode(url)
        current_tail, self.tail = self.current, self.current
        self.tail.next = node
        self.tail = node
        self.tail.prev = current_tail
        self.current = self.tail
  

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current == self.head:
                return self.head.val
            self.current = self.current.prev
        return self.current.val
            
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current == self.tail:
                return self.tail.val
            self.current = self.current.next
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
class LRUCache:

    def __init__(self, capacity: int):
        self.dict, self.capacity, self.list = {}, capacity, DoublyLinkedList()
        
    def get(self, key: int) -> int:
        if key not in self.dict:return -1
        self.updateNode(self.dict[key])
        return self.dict[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].val = value
            node = self.dict[key]
            self.list.moveNodeToTail(node)
        else:
            self.makeSpaceIfListIsFull()
            node = ListNode(key, value)
            self.dict[key] = node
            self.list.addNodeToTail(node)

    def updateNode(self, node) -> None:
        self.list.moveNodeToTail(node)

    def makeSpaceIfListIsFull(self):
        if len(self.dict) == self.capacity:
            self.dict.pop(self.list.head.key)
            self.list.removeHead()


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNodeToTail(self, node) -> None:
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def removeHead(self) -> None:
        newHead = self.head.next
        self.head.next = None
        if newHead:
            newHead.prev = None
        self.head = newHead

    def moveNodeToTail(self, node) -> None:
        if not node.next:
            return

        current_prev, current_next = node.prev, node.next
        if not current_prev:
            self.head = node.next
        else:
            current_prev.next = current_next
        current_next.prev = current_prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

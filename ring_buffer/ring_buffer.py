from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        if self.storage.length == self.capacity:
            # update current value
            self.current.value = item
            # if we're currently at the tail
            if self.current is self.storage.tail:
                # go back to head
                self.current = self.storage.head
            else:
                # else, go to the next
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
        self.current = 0

    def append(self, item):
        if self.current < self.capacity:
            self.storage.pop(0)
            self.storage.append((item))
        else:
            self.storage.pop(0)
            self.storage.insert(0, item)
            # self.storage[self.current] = item
            # self.storage.insert(self.current, item)
            self.current += 1

    def get(self):
        return [x for x in self.storage if x is not None]

import copy


class List:
    class Node:
        def __init__(self, val, next=None, prev=None) -> None:
            self.val = val
            self.next: None | List.Node = next
            self.prev: None | List.Node = prev

        def find_index(self, depth):
            if depth == 0:
                return self
            if self.next:
                return self.next.find_index(depth - 1)
            raise IndexError

        def find_next_value(self, val):
            if self.next:
                if self.next.val == val:
                    return self
                return self.next.find_next_value(val)

        def find_end(self):
            if self.next:
                return self.next.find_end()
            return self

        def print_list(self):
            print(self.val)
            if self.next:
                self.next.print_list()

    def __init__(self, val=None) -> None:
        self.root: List.Node = List.Node(val)
        self.len = 1

    def insert(self, index, val):
        if index >= self.len:
            self.append(val)
            return
        if abs(index) >= self.len or index == 0:
            old_root = self.root
            self.root = List.Node(val)
            self.root.next = old_root
            self.len += 1
            return
        old_node = self.get_index(index)
        new_node = List.Node(val, old_node)
        self.get_index(index - 1).next = new_node
        self.len += 1

    def pop(self, index=None):
        if not index:
            self.get_index(self.len - 2).next = None
        else:
            next = self.get_index(index).next
            self.get_index(index - 1).next = next
        self.len -= 1

    def append(self, val):
        self.root.find_end().next = List.Node(val)
        self.len += 1

    def remove(self, val):
        if self.root.val == val:
            self.root = self.root.next
            self.len -= 1
            return
        (x := self.root.find_next_value(val))
        if x:
            next = x.next.next
            if next:
                x.next = next
            else:
                x.next = None
            self.len -= 1
            return
        raise IndexError

    def print_list(self):
        self.root.print_list()

    def print_index(self, index):
        print(self.get_index(index).val)

    def get_index(self, index):
        return self.root.find_index(index)

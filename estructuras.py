"""Contiene Nodos, Listas, Pilas y Colas"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_first(self):
        return self.head

    def get_last(self):
        return self.tail

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        node = Node(e)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head = node

        self.size += 1

    def add_last(self, e):
        node = Node(e)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None

        temp = self.head
        self.head = temp.get_next()
        temp.set_next(None)
        self.size -= 1

        return temp.get_data()

    def remove_last(self):
        if self.size == 1:
            self.remove_first()
        else:
            temp = self.tail
            prev = self.head
            while prev.get_next() != self.tail:
                prev = prev.get_next()
            prev.set_next(None)
            self.tail = prev
            self.size -= 1

            return temp.get_data()


class DoubleNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev


class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def get_first(self):
        return self.head

    def get_last(self):
        return self.tail

    def add_first(self, data):
        new_head = DoubleNode(data)
        if self.is_empty():
            self.head = new_head
            self.tail = new_head
        else:
            self.head.set_prev(new_head)
            new_head.set_next(self.head)
            self.head = new_head

        self.size += 1

    def add_last(self, data):
        new_tail = DoubleNode(data)
        if self.is_empty():
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.set_next(new_tail)
            new_tail.set_prev(self.tail)
            self.tail = new_tail

        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        elif (self.size == 1):
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.get_next()
            temp.set_next(None)
            self.head.set_prev(None)
        self.size -= 1
        return temp.get_data()

    def remove_last(self):
        if self.is_empty():
            return None
        else:
            temp = self.tail
            self.tail = temp.get_prev()
            temp.set_prev(None)
            self.tail.set_next(None)
            self.size -= 1
        return temp.get_data()

    def remove(self, node):
        """Se asume que la lista contiene a node."""
        if self.head == node:
            return self.remove_first()
        elif self.tail == node:
            return self.remove_last()
        else:
            prev = node.get_prev()
            next = node.get_next()
            prev.set_next(next)
            node.set_prev(None)
            node.set_next(None)
            next.set_prev(prev)
            self.size -= 1
            return node.get_data()

    def add_before(self, data, node):
        """Se asume que la lista contiene a node."""
        if self.head == node:
            self.add_first(data)
        else:
            new_node = DoubleNode(data)
            prev = node.get_prev()
            prev.set_next(new_node)
            new_node.set_prev(prev)
            new_node.set_next(node)
            node.set_prev(new_node)
            self.size += 1

    def add_after(self, data, node):
        """Se asume que la lista contiene a node."""
        if self.tail == node:
            self.add_last(data)
        else:
            new_node = DoubleNode(data)
            next = node.get_next()
            node.set_next(new_node)
            new_node.set_prev(node)
            new_node.set_next(next)
            next.set_prev(new_node)
            self.size += 1

    # EXTRAS
    def as_pylist(self):
        new_list = []
        temp = self.get_first()
        while temp != None:
            new_list.append(temp.get_data())
            temp = temp.get_next()
        return new_list


class Stack:
    def __init__(self):
        self.data = List()

    def get_size(self):
        return self.data.get_size()

    def is_empty(self):
        return self.data.is_empty()

    def push(self, e):
        self.data.add_first(e)

    def pop(self):
        self.data.remove_first()

    def top(self):
        if self.is_empty():
            return None
        return self.data.get_first().get_data()


class Queue:
    def __init__(self):
        self.data = List()

    def get_size(self):
        return self.data.get_size()

    def is_empty(self):
        return self.data.is_empty()

    def enqueue(self, e):
        self.data.add_last(e)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.data.remove_first()

    def first(self):
        if self.is_empty():
            return None
        else:
            return self.data.get_first().get_data()

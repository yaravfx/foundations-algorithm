# Linked list example

# Singly-linked list
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data, index=0):
        # check if index is within bounds
        if index > self.count or index < 0:
            return

        new_node = Node(data)

        # Special case: inserting at the head
        if index == 0:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            i = 0
            current = self.head
            # iterate update to index to find previous node before the target position
            while i < index:
                _prev = current
                current = current.get_next()
                i += 1

            _prev.set_next(new_node)
            new_node.set_next(current)

        self.count += 1
        return True


    def find(self, val):
        """find the first item with a given value"""
        item = self.head
        # iterate through nodes until node with target value is found
        while item and item.value != val:
            _next = item.get_next()
            item = _next
        return item.value

    def deleteAt(self, index):
        # check if index is within bounds
        if index > self.count - 1:
            return

        current = self.head
        # Special case: deleting the head node
        if index == 0:
            self.head = current.get_next()
        else:
            i = 0
            current = self.head
            _prev = None
            # iterate update to index to find the previous node before the target position
            while i < index:
                _prev = current
                current = current.get_next()
                i += 1

            _prev.set_next(current.get_next())

        self.count -= 1
        return True

    def dump_list(self):
        temp = self.head
        while temp != None:
            print("Node: ", temp.get_data())
            temp = temp.get_next()


ll = LinkedList()
ll.insert("A")
ll.insert("B")
ll.insert("C", 1)


ll.dump_list()
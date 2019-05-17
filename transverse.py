class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def printList(self):
        value = self.head

        while value != None:
            print(value.data)
            value = value.next


first = Linked()

#buat node
first.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

#hubungkan antar node
first.head.next = second
second.next = third
third.next = fourth

first.printList()

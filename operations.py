class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    #insert data di awal
    def shift(self, newValue):
        newNode = Node(newValue)

        newNode.next = self.head
        self.head = newNode

    #insert data di akhir
    def push(self, newValue):
        newNode = Node(newValue)

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    #mengambil data paling awal
    def unshift(self):
        return self.head

    #mengambil data paling akhir
    def pop(self):
        last = self.head

        while last.next != None:
            last = last.next

        return last.data

    def printVal(self):
        value = self.head

        while value != None:
            print(value.data)
            value = value.next




#inisiasi
first = Linked()
first.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

#hubungkan antar node
first.head.next = second
second.next = third
third.next = fourth

first.shift("Shifted")
first.push("Push Success")

first.printVal()

foremost = first.unshift()
lattermost = first.pop()

print("")

print("Data paling awal : " + foremost.data)
print("Data paling akhir : " + lattermost)

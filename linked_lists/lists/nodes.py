class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def appendToTail(self, data):
        new_node = Node(data)
        # with new_node, check list has any items
        if self.head is None:
            self.head = new_node
            return

        # if list has items, cycle thru LL until finding empty "next"
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        # then insert new node into the empty "next"
        current_node.next =  new_node

    def appendToStart(self, data):
        # create new Node
        new_node = Node(data)
        # insert at beginning if empty
        if self.head is None:
            self.head = new_node
            return
        # if not empty, put head at new_node next attribute
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        # if index is zero
        if (index == 0):
            self.appendToStart(data)

        # iterate through LL to index or empty node.
        position = 0
        current_node = self.head
        while(current_node != None and position + 1 != index):
            position += 1
            current_node = current_node.next

        # tag tail onto new node, then put new node in as tail
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("index not present")

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    def deleteFirstNode(self):

        if (self.head == None):
            return

        self.head = self.head.next

    def deleteLastNode(self):
        if (self.head == None):
            return
        current_node = self.head
        while (current_node.next != None and current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None

    def removeAtIndex(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0

        if index == 0:
            self.deleteFirstNode()
        else:
            while current_node is not None and position < index - 1:
                position += 1
                current_node = current_node.next

            if current_node is none or current_node.next is None:
                print("Index not present")
            else:
                current_node.next = current_node.next.next

    def removeNode(self, data):
        current_node = self.head

        # check if the head node contains the data
        if current_node.data == data:
            self.deleteFirstNode()
            return
        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

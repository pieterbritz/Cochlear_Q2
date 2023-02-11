class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def AddToBegining(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

    # Function to add a new node
    def AddToEnd(self, newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    # Function to delete a node
    def DeleteNode(self, removekey):
        headVal = self.head            
        if headVal is not None:
            if headVal.data == removekey:
                self.head = headVal.next
                headVal = None
                return
        while headVal is not None:
            if headVal.data == removekey:
                break
            prev = headVal
            headVal = headVal.next
        if headVal == None:
            return
        prev.next = headVal.next
        headVal = None
        
    # Function to calculate the number of nodes in the list
    def CalculateNumberOfNodes(self):
        start = self.head
        total = 0
        while start is not None:
            total += 1
            start = start.next
        return total  

    # Function to print the linked list
    def PrintList(self):
        printVal = self.head
        while printVal is not None:
            print (printVal.data)
            printVal = printVal.next
    
    # Function to print the linked list in reverse
    # If the list was a boubly list, 
    #   the previous node reference could have been used
    def PrintListInReverse(self):
        tmp = SLinkedList()
        headVal = self.head           
        while headVal is not None:
            tmp.AddToBegining(headVal.data)
            headVal = headVal.next
        tmp.PrintList()


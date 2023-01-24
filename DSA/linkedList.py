class Node :
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList : 
    def __init__(self,value): 
        
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self) :

        temp = self.head
        while temp is not None :
            print(temp.value)
            temp = temp.next


    def append(self,value) :

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1 
        return True

    def pop(self) :

        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value


linkedlist = LinkedList(4)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.printList()
linkedlist.pop()
linkedlist.printList()

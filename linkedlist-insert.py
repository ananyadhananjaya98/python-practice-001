class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addfront(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def addlast(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def insert_pos(self,data,pos):
        newnode = node(data)
        prev_node = None
        cur_node = self.head
        count =1
        temp = self.head
        while temp != None:
            count+=1
            temp = temp.next
        if count < pos:
            print("Enter valid position!")
            exit()
        if count == pos:
            self.addlast(data)
            return
        if pos == 1:
            self.addfront(data)
            return
        count = 1
        while cur_node != None:
            if count ==pos:
                prev_node.next = newnode
                newnode.next = cur_node
            prev_node = cur_node
            cur_node = cur_node.next
            count+=1

    def printlist(self):
        temp = self.head
        while temp!= None:
            print(temp.data)
            temp= temp.next

newlist = linkedlist()
newlist.addfront("milk")
newlist.addfront("bread")
newlist.addlast("butter")
newlist.insert_pos("eggs",5)
newlist.printlist()

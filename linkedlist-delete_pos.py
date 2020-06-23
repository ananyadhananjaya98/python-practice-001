class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addlast(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            x = self.tail
            x.next = newnode
            self.tail = newnode

    def addfront(self, data):
        newnode = node(data)
        if self.head == None:
            self.head= newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def poplast(self):
        next_node = self.head
        if next_node.next != None:
            next_node = next_node.next
        deletenode = next_node.next
        next_node.next = None
        self.tail = next_node
        del deletenode

    def popfront(self):
        deletenode = self.head
        del deletenode
        secondnode =self.head.next
        self.head = secondnode

    def insert_pos(self,data,pos):
        newnode = node(data)
        count = 0
        if pos == 0:
            self.addfront(data)
            return
        temp = self.head
        while temp != None:
            count+=1
            temp = temp.next
        if count ==pos:
            self.addlast(data)
            return
        if pos > count:
            print("Enter valid position!")
            return
        count = 0
        prev_node = None
        cur_node = self.head
        while count <= pos:
            if count == pos:
                prev_node.next = newnode
                newnode.next = cur_node
                return
            else:
                prev_node = cur_node
                cur_node = prev_node.next
                count+=1

    def delete_pos(self,pos):
        count = 0
        if pos == 0:
            self.poplast()
            return
        temp =self.head
        while temp != None:
            count+=1
            temp = temp.next
        if count == pos:
            self.poplast()
            return
        if pos > count:
            print("Enter valid position!")
            return
        count = 0
        prev_node = None
        cur_node = self.head
        while count<= pos:
            if count == pos:
                prev_node.next = cur_node.next
                #cur_node = prev_node.next
                return
            else:
                prev_node = cur_node
                cur_node = prev_node.next
                count+=1



newlist = linkedlist()

newlist.addlast("milk")
newlist.addlast("sugar")
newlist.addlast("bread")
newlist.addlast("teabags")
newlist.insert_pos("tea",4)
newlist.display()
print()
newlist.delete_pos(2)
newlist.display()

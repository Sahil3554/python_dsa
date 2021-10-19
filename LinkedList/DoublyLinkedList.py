class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_at_begining(self,data):
        n = Node(data)
        n.next=self.head
        # Setting Link to previous Node if Exist
        if self.head!=None:
            self.head.prev=n
        self.head=n
        #  Setting Tail as Current Node if List is Empty
        if self.tail==None:
            self.tail=n
    # Insert at the end of Linked List
    def insert_at_end(self,data):
        n= Node(data)
        #  if List is Empty Insert at begining
        # Reusing The Code
        if self.head==None:
            self.insert_at_begining(data)
        else:
            n.prev=self.tail
            self.tail.next=n
            self.tail=n
    # Insert Many Value in Linked List        
    def insert(self,*data_list):
        for item in data_list:
            self.insert_at_end(item)

    # Delete From Given Index of Linked List
    def delete_by_index(self,index):
        if index==0:
            self.delete_at_start()
        else:
            itr=self.head
            count=0
            while itr:
                if count==index-1:
                    itr.next=itr.next.next
                if count==index+1:
                    itr.prev=itr.prev.prev    
                    break
                itr=itr.next
                count+=1

    # Delete From Start of Linked List
    def delete_at_start(self):
        self.head=self.head.next
        self.head.prev=None
    # Give the length of Linked List
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count+=1
        return count
    def insert_after_value(self,value,data):
        n = Node(data)
        itr= self.head
        while itr:
            if itr.data==value:
                temp=itr.next
                itr.next=n
                n.next=temp
                n.prev=itr
                n.next.prev=n
                break
            itr=itr.next
    def remove_by_value(self,value):
        itr= self.head
        while itr:
            if itr.data==value:
                if itr.prev!=None:
                    itr.prev.next=itr.next
                else:
                    self.head=itr.next
                if itr.next!=None:
                    itr.next.prev=itr.prev
                else:
                    self.tail=itr.prev
                # itr.next=itr.next.next
                break
            itr=itr.next
    def delete_at_end(self):
        self.tail=self.tail.prev
        self.tail.next=None    
    # Print Linked List Fowrard
    def printForward(self):
        itr =self.head
        list_data=""
        while itr:
            list_data+=str(itr.data)+"-->"
            itr= itr.next
        print(list_data)
    # Print Linked List Backwrard
    def printBackward(self):
        itr =self.tail
        list_data=""
        while itr:
            list_data+=str(itr.data)+"<--"
            itr= itr.prev
        print(list_data)

if __name__=="__main__":
    ll = DoublyLinkedList()
    ll.insert(12,1,13,14,5)
    ll.printForward()    
    ll.insert_at_begining(3)
    ll.insert_at_begining(5)
    print("After Inserting 3,5 at begining")
    ll.printForward()
    print("Inserting 19 After 1")
    ll.insert_after_value(1,19)
    ll.printForward()

    ll.insert_at_end(15)    
    print("After Inserting 15 at end")
    ll.printForward()
    
    ll.delete_at_end()    
    print("After Removing Last Element")
    ll.printForward()

    ll.remove_by_value(1)    
    print("After Removing Element 1")
    ll.printForward()

    ll.remove_by_value(5)    
    print("After Removing Element 5")
    ll.printForward()

    ll.remove_by_value(5)    
    print("After Removing Element 5")
    ll.printForward()

    ll.remove_by_value(19)    
    print("After Removing Element 19")
    ll.printForward()
    # Printing Linked List Backwrard
    ll.printBackward()
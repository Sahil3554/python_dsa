# Linked List Implementattion in python
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    # Insert at the begining of Linked List
    def insert_at_begining(self,data):
        n = node(data)
        n.next=self.head
        self.head=n

    # Insert at the end of Linked List
    def insert_at_end(self,data):
        n= node(data)
        if self.head==None:
            self.head=n
        else:
            itr=self.head
            while itr.next:
                itr =itr.next
            itr.next =n
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
                    break
                itr=itr.next
                count+=1

    # Delete From Start of Linked List
    def delete_at_start(self):
        self.head=self.head.next
    # Give the length of Linked List
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count+=1
        return count
    def insert_after_value(self,value,data):
        n = node(data)
        itr= self.head
        while itr:
            if itr.data==value:
                temp=itr.next
                itr.next=n
                n.next=temp
                break
            itr=itr.next
    def remove_by_value(self,value):
        itr= self.head
        while itr:
            if itr.next.data==value:
                itr.next=itr.next.next
                break
            itr=itr.next
    def delete_at_end(self):
        itr= self.head
        while itr:
            if itr.next.next==None:
                itr.next=None
                break
            itr=itr.next
    # Print Linked List
    def printList(self):
        tmp =self.head
        list_data=""
        while tmp:
            list_data+=str(tmp.data)+"-->"
            tmp= tmp.next
        print(list_data)

if __name__=="__main__":
    ll = LinkedList()
    ll.insert(12,1,13,14,5)
    ll.printList()    
    ll.insert_at_begining(3)
    ll.insert_at_begining(5)
    print("After Inserting 3,5 at begining")
    ll.printList()
    ll.insert_at_end(15)

    print("After Inserting 15 at end")
    ll.printList()

    print("After Deleting element at index 3")
    ll.delete_by_index(3)
    ll.printList()
    print("After Deleting element at index 0")
    # ll.delete_by_index(0)
    ll.delete_at_start()
    ll.printList()
    print("length of list is",ll.get_length())

    print("After Deleting element at last index")
    # last_index= ll.get_length()-1
    # ll.delete_by_index(last_index)
    ll.delete_at_end()
    ll.printList()
    print("Inserting 12 after 13")
    ll.insert_after_value(13,12)
    ll.printList()
    print("After Removing 12")
    ll.remove_by_value(12)
    ll.printList()
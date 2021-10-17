# Hash Table Using Python List(Collision Not Handled)
class HashTable:
    def __init__(self):
        self.MAX = 10;
        self.list = [None for i in range(self.MAX)]
    def gethash(self,key):
        hash_sum=0
        for character in key:
            hash_sum+=ord(character)
        return hash_sum%10
        
    def __setitem__(self,key,value):
        hash =  self.gethash(key)
        self.list[hash]=value
    def __getitem__(self,key):
        hash =  self.gethash(key)
        return self.list[hash]

    def __delitem__(self,key):
        hash =  self.gethash(key)
        self.list[hash] =None
h = HashTable()
print("Initial List")
print(h.list)
h['sahil']=3
print("Sahil:",h['sahil'])
print("List After Insertion")
print(h.list)
del h['sahil']
print("List After Deletion")
print(h.list)

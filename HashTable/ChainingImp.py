class HashTable:
    def __init__(self):
        self.MAX = 10;
        self.list = [[] for i in range(self.MAX)]
    def gethash(self,key):
        hash_sum=0
        for character in key:
            hash_sum+=ord(character)
        return hash_sum%10
        
    def __setitem__(self,key,value):
        hash =  self.gethash(key)
        self.list[hash].append((key,value))
    def __getitem__(self,key):
        hash =  self.gethash(key)
        for index,item in enumerate(self.list[hash]):
            if key==item[0]:
                return item[1]
        return -1

    def __delitem__(self,key):
        hash =  self.gethash(key)
        for index,item in enumerate(self.list[hash]):
            if key==item[0]:
                del self.list[hash][index]
h = HashTable()
print("Initial HashTable")
print(h.list)
h['sahil']=3
h['ab']=4
h['ba']=5
print("Sahil:",h['sahil'])
print("ab:",h['ab'])
print("ba:",h['ba'])
print("HashTable After Insertion")
print(h.list)
del h['sahil']
print("HashTable After Deletion")
print(h.list)

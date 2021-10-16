def BinarySearch(start,end,items,element):
    # print("Start:",start,"end:",end,"items",items[start:end+1],"el:",element)
    mid = (start+end)//2
    # print("mid",mid)
    # print(items[mid]==element)
    if items[mid]==element:
        # print("middle element",mid)
        return mid
    elif start!=end:
        if items[mid]>element:
            return BinarySearch(start,mid-1,items,element)
        elif items[mid]<element:
            return BinarySearch(mid+1,end,items,element)
    else:
       return -1        

test_cases = [{
    "input":{
        "items":[1,2,3,4,4,5,6],
        "element":5
    },
    "output":5
},{
    "input":{
        "items":[1,2,3,4,4,6],
        "element":5
    },
    "output":5
},{
    "input":{
        "items":[1,2,3,4,4,6],
        "element":5
    },
    "output":-1
},{
    "input":{
        "items":[1,2,3,4,4,6],
        "element":4
    },
    "output":4
},{
    "input":{
        "items":[1,2,3,4,4,6],
        "element":4
    },
    "output":5
}]
for count,test in enumerate(test_cases):
    print("Test Case #",count)
    result = BinarySearch(0,len(test["input"]["items"])-1,test["input"]["items"],test["input"]["element"])
    if result==test["output"]:
        print("Pass")
    else:
        print("Fail")
    
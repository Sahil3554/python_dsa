def linear_search(items,element):
    for position,item in enumerate(items):
        if item==element:
            return position
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
    "output":-1
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
    "output":3
},{
    "input":{
        "items":[1,2,3,4,4,6],
        "element":3
    },
    "output":2
}
]
for count,test in enumerate(test_cases):
    print("Test Case #",count)
    result = linear_search(**test["input"])
    if result==test["output"]:
        print("Pass")
    else:
        print("Expected:",test["output"])
        print("Actual:",result) 
        print("Fail")
    
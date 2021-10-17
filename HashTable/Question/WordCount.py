#Write Program to Take A String As Input And Output the Key Value pair of total number of time charcters are present 
def count_char(input_string):
    dict={}
    # input_string = input()

    for char in input_string:
        if(dict.get(char,False)):
            dict[char]=dict[char]+1
        else:
            dict[char]=1
    return dict
print(count_char("Sahil Tagra"))
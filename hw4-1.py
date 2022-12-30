##● Write a function merge_str that given two strings of the same
##length merges them returning a single string which containing all
##the characters of the two strings merged as follows:
##● String 1: “abcdefghil”
##● String 2: “pippopluto”
##● Returns: “apbicpdpeofpglhuitlo”

def merge_str(string1,string2):
    string4=""
    for i in range(0,len(string1)):
        string3=string1[i]+string2[i]
        string4=string4+string3
    return string4
        


string1="abcdefghil"
string2="pippopluto"
print(merge_str(string1,string2))

#Teacher's version

def merge_str(string1,string2):
    ms=""
    i=0
    while i<len(string1):
        if string1[i].lower()<string2[i].lower():
            ms=ms+string1[i]+string2[i]
        else:
            ms=ms+string2[i]+string1[i]
        i+=1
    return ms


string1="abcdefghil"
string2="pippopluto"
print(merge_str(string1,string2))

##● Write a function compare_strings which takes two strings and
##return True if the first string comes first in the alphabet than the second one
##(Otherwise it returns False). NB You should consider strings
##including both lower case and upper case letters and the standard
##alphabetical sorting rules.
##● Hint: the module string contains two constants string.lowercase
##and string.uppercase that include all the letters. You can check for
##uppercase letters with the condition char in string.uppercase.


def compare_string(string1,string2):
    L_string1=string1.lower()
    L_string2=string2.lower()
    if L_string1<L_string2:
        return True
    else:
        return False
    
        
        

string1=input("insert string: ")
string2=input("insert string: ")
print(compare_string(string1,string2))

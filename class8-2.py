#sublist

def sublist(L1,L2):
    if len(L1)>len(L2):
        return False
    else:
        m=len(L1)
        i=0
        while i<len(L2)-m+1: #len(L2)-m is the part of L2 im comparing to L1
            if L1==L2[i:m+i]:
                return True
            i+=1
        return False

print(sublist([1,2],[1,2,3,4]))
print(sublist([1,4],[1,2,3,4]))


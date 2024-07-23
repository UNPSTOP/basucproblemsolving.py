#User function Template for python3
def isSubset( a1, a2, n, m):
    se1=set(a1)
    set2=set(a2)
    count=0
    for x in se1:   
        if x in set2:
          count +=1
    if count==len(set2):
        return "Yes"
    return "No"
s="output"
# s=list(s)
list1=[]
h=0
for i in range(1,len(s)):
    if s[h] == s[i]:
        list1.append(s[h])
        h+=1
   
    else:
        h+=1   
print(list1)        

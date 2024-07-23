s=s="c?zaicq"
print(s)
count=0
count2=0
for i in  range(0,len(s)):
    if s[i] in 'aioue?':
        count +=1
    elif s[i] not in 'aioue?':
        count2 +=1
if count2 >=3 or count >=5:
    print("bad")
else:
    print("goood")
print(count,count2)
print(s)
count=0
count2=0
for i in  range(0,len(s)):
    if s[i] in 'aioue':
        count +=1
    elif s[i] not in 'aioue?':
        count2 +=1
if count2 >3 or count >5:
    print("bad")
else:
    print("goood")
print(count,count2)
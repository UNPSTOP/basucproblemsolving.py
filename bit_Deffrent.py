# a=10
# a=bin(a)
# a=a[2:]
# b=20
# b=bin(b)
# b=b[2:]
# print(a,b)
# count=0
# x=int(a)+int(b)
# x=str(x)
# for i in range(len(x)):
#     if x[i]=='1':
#         count +=1
#     else:
#         pass
# print(count)
# # dismil to bimary
num=19
digit=[]
while num>0:
    if num %2==0:
       digit.append(0)
    else:
        digit.append(1)
    num//=2
digit.reverse()
print(digit)

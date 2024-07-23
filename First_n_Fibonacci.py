n=5
if n<0:
    print(0)
elif n==1:
    print(0)
sequen=[1,1]
for i in range(2,n):
    value=sequen[-1]+sequen[-2]
    sequen.append(value)
print(sequen)
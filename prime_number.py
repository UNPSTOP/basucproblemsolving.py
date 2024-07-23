n=55
if n <=1:
    print(0)
for i in range( 2, int(n**0.5)+1):
    if n % i ==0 :
       print(0)
    else:
       print(1)
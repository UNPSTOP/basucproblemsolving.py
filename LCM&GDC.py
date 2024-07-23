tn1=a
tn2=b
while a%b !=0:
    r =a%b
    a=b
    b=r
    gdc=b
    lcm=(tn1*tn2)//gdc
return lcm,gdc
a = int(input("please input a number a:"))
b = int(input("please input a number b:"))
c = int(input("please input a number c:"))
if (a<b):
    t=a
    a=b
    b=t
if (a<c):
    t=a 
    a=c
    c=t
if (b<c):
    t=b
    b=c
    c=t
print ("sort result:",a,b,c)


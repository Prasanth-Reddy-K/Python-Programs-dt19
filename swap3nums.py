a= int(input("Enter a value : "))
b= int(input("Enter b value : "))
c= int(input("Enter c value : "))
if(a>=b and a>=c):
    if b> c:
        temp =a
        a=c
        c= temp
    else :
        temp1=a
        temp2=b
        temp3=c
        c=a
        a= b
        b= temp3
else:
    if b>c and a>c:
        temp1=a
        temp2=b
        temp3=c
        c= b
        a= temp3
        b= temp1
    else:
        temp =a
        a=c
        c= temp
print("After sorting the elements", a,b,c)
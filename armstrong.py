num= int(input("Enter number : "))
rev=0
c=0
temp1=temp2= num
while( num!=0):
    num//=10
    c+=1
while( temp2!=0):
    rem= temp2%10
    rev= rev + rem**c
    temp2//=10
if temp1== rev:
    print("Yes")
else :
    print("no")
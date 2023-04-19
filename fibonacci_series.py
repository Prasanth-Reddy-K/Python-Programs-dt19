num= int(input("Enter the count : "))
count=3
a=0
b=1
if(num<2):
    print("Please enter positiv num")
else:
    print(a,b, end= " ")
    while(count<=num):
        c= a+b
        a=b
        b=c
        count+=1
        print(c, end= " ")
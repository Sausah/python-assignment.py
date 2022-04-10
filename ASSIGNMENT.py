print("Calculator")
print("1.Add")
print("2.Substract")

# input choice
ch=int(input("Enter Choice(1-100): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
else:
    print("Invalid Choice")

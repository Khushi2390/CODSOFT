print("1-Addition")
print("2-Subtract")
print("3- Multiply")
print("Division")
option=int(input("Choose an operation: "))

if(option in[1,2,3,4]):
num1= int(input("Enter first operation:  "))
num2= int(input("Enter first operation:  "))

if(option== 1):
result= num1+num2

eLif(option== 2):
result= num1-num2

elif(option== 3):
result= num1*num2

elif(option== 4):
result= num1 // num2
else:
    print("invalid opertion entered")
    
    print("The result of the operation is {}".format(result))

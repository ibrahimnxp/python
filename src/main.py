print("welcome to the calculator")
print("select an operation:")
print("1. ADD")
print("2. SUBTRACT")
print("3. DIVIDE")
print("4. MULTIPLY")

operation =input()

if operation =="1":
   num1 = input("Enter Number1:")
   num2 = input("Enter Number2:")
   print("Total Is " + str(int(num1)+int(num2)))
elif operation =="2":
     num1 = input("Enter Number1:")
     num2 = input("Enter Number2:")
     print("Total Is " + str(int(num1)-int(num2)))
elif operation =="3":  
     num1 = input("Enter Number1:")
     num2 = input("Enter Number2:")
     print("Total Is " + str(int(num1)/int(num2)))
elif operation =="4":   
     num1 = input("Enter Number1:")
     num2 = input("Enter Number2:")
     print("Total Is " + str(int(num1)*int(num2)))
else:
     print("Invalid Entry")





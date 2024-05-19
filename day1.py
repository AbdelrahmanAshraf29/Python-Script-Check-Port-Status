def add (x , y):
    return x + y 
def substract ( x, y ):
    return x - y
def multiply ( x , y):
    return x * y
def divide ( x , y):
    if  y == 0:
        return " Error! unkniw Result"
    else:    
        return x / y

print (" Welcome to My calculator!")
print (" Choose the following operations:")
print("1. Add ")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
print ("5. Exit")
while True:
    choice = input("Enter choice (1-2-3-4-5):")
    if choice in ('1', '2' , '3' , '4' ):
        num1 = float(input("Enter first numb: "))
        num2 = float (input("Enter Second numb: "))

        if choice == '1':
            result = add (num1,num2)
        elif choice == '2':
            result = substract(num1 , num2)
        elif choice == '3':
            result = multiply (num1 , num2)
        elif choice == '4':
            result = divide ( num1 , num2)

        print(" The Result is: ", result)
    elif choice == '5':
        print ("Exit")    
        break
    else:
        print(" Please choose the correct input")

        
    if input("Do you want to perform another operation? (yes/no): ").lower() != 'yes':
        break
'''
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
'''
'''
while True:
    try:
        numb1 = float (input("Enter first Number: "))
        numb2 = float (input("Enter Second number:"))
        result = numb1 / numb2
        print("The Result is: ", result)
        choice = input("Do you want to perform another operation? (yes/no): ").lower()
        if choice != 'yes':
           break
    except ValueError:
        print("Please Inser valid value")
    except ZeroDivisionError:
        print("Error Dont Divide by zero")
 '''
'''
bill_amount = 47.28
tip_perc = 0.15
friends = 2

tip_amount = tip_perc * bill_amount
total_amount = tip_amount + bill_amount

share = total_amount / friends 

print ("The tip amount is " , tip_amount)
print ("The Total amount is " , total_amount)
print ("Each one of them will pay" , share)
'''

'''
statement = input ("Enter Your statement")
length = len(statement)
print ("length of statement", length)
'''

'''
word1 = "how"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "{}"
word6 = "so"
word7 = "far?"
word7 = word7.replace ('?' , '!')

sentence = f"{word1} {word2} {word3} {word4} {word5} {word6} {word7}"
print(sentence)

'''
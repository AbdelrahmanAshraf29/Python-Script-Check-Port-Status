import math

'''
sentence = input("Enter your string")
index = list (index for index, char in enumerate(sentence) if char == 'i')
print ("Index of i" , index)
'''

'''
def cal_area(shape , base = 0 , height = 0 , width = 0 , radius = 0):
    if shape == "Triangle":
        return 0.5 * base * height
    elif shape == "Rectangle":
        return width * height
    elif shape == "Square":
        return width * height
    elif shape == "circle":
        return math.pi * radius ** 2
    else:
        return " Invalid Choice"
    
t_area = cal_area ("Triangle" ,  base = 10 , height = 7 )
print("Area of triangle is:" , t_area)

rec_area = cal_area ("Rectangle" ,  width = 10 , height = 7 )
print("Area of Rectangle is:" , rec_area)

square_area = cal_area ("Square" , width = 10 , height = 10 )
print("Area of Square is:" , square_area )

cir_area = cal_area ("circle" ,  radius = 10  )
print("Area of Circle is:" , cir_area)
'''
'''
def cal_area(shape , num1  , num2 = 0):
    if shape == "Triangle":
        return 0.5 * num1 * num2
    elif shape == "Rectangle":
        return num1 * num2
    elif shape == "Square":
        return num1 * num2
    elif shape == "circle":
        return math.pi * num1 ** 2
    else:
        return " Invalid Choice"
    
t_area = cal_area ("Triangle" ,  num1 = 10 , num2 = 7 )
print("Area of triangle is:" , t_area)

rec_area = cal_area ("Rectangle" ,  num1 = 10 , num2 = 7 )
print("Area of Rectangle is:" , rec_area)

square_area = cal_area ("Square" , num1 = 10 , num2 = 10 )
print("Area of Square is:" , square_area )

cir_area = cal_area ("circle" ,  num1 = 10  )
print("Area of Circle is:" , cir_area)
'''

'''
def gen_table (number):
    table = []
    for i in range ( 1 , number + 1 ):
        x = [i * j for j in range (1 , i +1)]
        table.append(x)
        return table
number = int (input("Ente your Number:"  ))
multiply_table = gen_table(number)
print(multiply_table)
'''
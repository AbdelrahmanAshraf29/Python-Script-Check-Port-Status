import re
from myexperiance.files.fileoperation import readfromfile
s=readfromfile('asd.txt')
emailpattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
print(re.match(emailpattern,s))#string started with email
print(re.fullmatch(emailpattern,s))#string all email
print(re.search(emailpattern,s))#string started with email
print(re.findall(emailpattern,s))#string started with email
# lines=s.split('\n')
# count=0
# for line in lines:
#     data=line.split(":")
#     if(data[len(data)-1]=='error'):
#         count+=1
# print(count)
# import sys
# print(sys.argv)

# import os
# if(os.name!='nt'):
#     os.chdir('/var/www/html/')
#     print(os.system('ls'))
# else:
#     os.chdir(r'C:\www\html')
#     print(os.system('dir'))

# import math
# print(math.pi)


# from myexperiance.files.fileoperation import writetofile
# writetofile('ddd','ddd')
# from myexperiance.mymath import sub as mymathsub
# def sub():
#     print('day3 sub')
# sub()
# mymathsub()

# import myexperiance.mymath
# myexperiance.mymath.sum()
# from myexperiance.files.fileoperation import *
# writetofile('asd3','kdflksdfk')
# import fileoperation
# fileoperation.writetofile('asd.txt',"""Line1
#                           alex
#                           sys admin""")
# fileoperation.writetofile('asd2.txt',"""smart
#                           devopes""")
# #open append
# f1=open('asd.txt','r+')
# #write
# if(f1.writable()):
#     s=f.read()

#     f1.seek(0)
#     f1.write('\nalex')
    

# #close
# f1.close()







# # #open  path write
# # f=open('asd.txt','w')
# # print(type(f))
# # if(f.writable()):
# #     f.write('ddd')
# #     f.write('''line2
# #             line3''')
# #     l=['line4','line5']
# #     f.writelines(l)
# #     #  f.read()
# # #close
# # f.close()

# # #open r
# # f1=open('asd.txt','r')
# # if(f1.readable()):
# #     for lline in f1:
# #         print(lline)
# #     # print(f1.readlines())
# #     # print(f1.readline())
# #     # s=f1.read(2)
# #     # print(s)
# #     # s=f1.read()
# #     # print('==',s)
# # #close
# # f1.close()



# try:
#     # print(1/0)#zero
#     n1=int(input('enter n1'))#casting
#     n2=int(input('enter n2'))
# except ValueError:
#     print('n1,n2 must be numbers')
# except ZeroDivisionError:
#     print('cannt to divid by zero')
# except:#exception
#     print('error')
# else: #only try done
#     print('all sevrer backuped')
# finally:#try done or except
#     print('thnx for using')

# n1=input('enter n1')
# if(n1.isdigit()):
#     n1=int(n1)
# else:
#     print('enter number')
# n2=int(input('enter n2'))
# print(n1+n2)
# name='global'#global var
# def fun1():
#     name='fun1'
#     def fun2():
#         global name #access first local var in hi. scope
#         print(name)#1 only access
#         name='fun2'#try modified scope fun1
#     fun2()
#     print(name)#1
# fun1()
# print(name)
# # n1=int(input('enter n1'))
# n2=int(input('enter n2'))
# def mysum(n1,n2):    
#     print(n1+n2)

# mysum(n1,n2)
#read file
# mysum(2,3)






# x,y,z=1,2.2,True #unpacking
# print(x,y,z)
# #function param unlimited----->(key,value)
#function param unlimited---->value 
# def connectssh(**param):#collection of user & pass --->dict
#     print(param,type(param))#((1,2,3))
# fun(key='v',k2=23)#calling values--->dict packing
# #function param [2,3]--->default arg
# def mysum(x,y,z=0):
#     pass
# def calarea(name,dim1,dim2=None):
#     #generic
#     pass
# calarea('c',10)#static
# name=input('enter shape name')
# calarea(name,dim1=1)

# mysum(1,3)
# mysum(1,2,3)


# # ips=[192.168.5.10]
# # password=('123456','')
# TraineeData={
#     'id':1,
#     'name':"aya ali",
#     'track':'sys admin',
#     'branch':'alex',
#     'grades':(100,99,85),
#     'id':200,
    
# }
# TraineeData['id']=100
# TraineeData['ID']=100#append new key ID --->100
# #+*---->dict1+dict2,dict*3
# for key,value in TraineeData.items():
#     print('key',x)
# TraineeData['grades'][0]=0
# varname={}
# print(type(varname))
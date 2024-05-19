import sys
import socket
ips=sys.argv[1]
# for ip in (ips):
try:
    hostname=socket.gethostbyname(ips)
# if(hostname is not None):        
    for port in range(1,65535):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)        
        res=s.connect_ex((hostname,port))
        if(res==0):
            print('port',port," is opened")
        s.close()
except KeyboardInterrupt:
    print('exsit program')
except socket.gaierror:
    print('hostname  coiuldnt be resolved')
except socket.error:
    print('server not responding!!!')

# import openpyxl

# from Employee import *
# emp1=Employee(1,'farah',8000)
# print(emp1.name)
# emp1.speak()
# print(emp1)
# x=1
# print(x)
# print(len('sdsd'))
# print(len([2,3.3,5,'dfdf']))
# print(len(emp1))
# # import Person
# print(Person.pi)

# # from Person import Person
# #object 
# # print('count',Person.count)

# # obj1=Person(1,'ali')#====>constructor(Person class) special function calling
# # obj2=Person(2,'aya')
# # obj3=Person()
# # Person.mtemp(37)
# # Person.incrementcount()
# # obj1.incrementcount()

# # print(obj1)
# # obj1.eat()
# # obj2.eat()
# obj3.eat()

# obj3.count=10


# print('count',Person.count)
# print('count',obj1.count)
# print('count',obj2.count)
# print('count',obj3.count)

# print('count',Person.count)
# print('count',obj1.count)
# print('count',obj2.count)
# obj3=Person()
# obj3.name='syed'
# obj3.id=100
# obj1.name='Ali'
# print(obj1.name)
# print(obj2.name)
# print(obj3.name)
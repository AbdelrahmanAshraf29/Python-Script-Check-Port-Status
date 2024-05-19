#define function,class,var
pi=3.14
class Person:
    count=0
    #define perporties,methods
    def __init__(self,id,name) -> None:
        #instance variable
        # print(type(self),self)
        self.id=id
        self.name=name
        # print('iam person const')
        Person.count+=1
    def speak(self):
        # print(self)
        print('iam ',self.name)
    @classmethod
    #self send ref to obj
    #self class name
    def incrementcount(cls):#chanhge instance to class method
        cls.count+=1

    @staticmethod
    def mtemp(temp):
        print(temp)
        if(temp>37):
            print('hot')
        elif(temp<37):
            print('cold')
        else:
            print('normal')
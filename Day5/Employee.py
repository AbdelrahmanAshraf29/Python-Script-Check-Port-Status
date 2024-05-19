from Person import *
class Employee(Person):
    def __init__(self, id, name,salary) -> None:
        super().__init__(id, name)
        self.salary=salary
    def __len__(self):
        return len(int(self.salary))
    # def speak(self):
    #     print('iam ',self.name,self.salary)
    # def __str__(self) -> str:
    #     return 'Iam employee '+self.name
class X(Employee):
    pass
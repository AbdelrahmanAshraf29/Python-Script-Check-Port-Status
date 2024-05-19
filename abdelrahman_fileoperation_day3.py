def read(path=input("Enter the path of the file : ")):
    file = open(path,'r')
    if(file.readable):
        print(file.readlines())
    file.close


def write(path=input("Enter the path of the file : "),
             content=input("Enter the content : ")):
    file= open(path,'w')
    if(file.writable):
        file.write(content)
    file.close


def append(path=input("Enter the path of the file : "),
              content=input("Enter the content : ")):
    file = open(path,'a')
    if(file.writable()):
        file.write("\n" + content)
        file.close()
    else:
        print("This file doesn't have write permission")
    
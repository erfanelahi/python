
from datetime import date
from datetime import datetime
from datetime import timedelta
import calendar
import os
from os import path
import shutil
from zipfile import ZipFile
import urllib.request

def power(a, b=1):
    result = 1
    for i in range(b):
        result = result * a
    return result 

def multi_add(*args):
    result = 0
    for i in args:
      result = result + i
    return result

def condition():
    x, y = 5, 9
    if x > y:
        print("x > y")
    elif x == y:
        print("x == y")
    else:
        print("y > x")

class myClass():
    def myDef1(self):
        print("This is myDef1")
    def myDef2(self, addMessage):
        print("This is myDef2 and {}".format(addMessage))
class anotherClass(myClass):
    def anotherDef1(self):
        myClass.myDef1(self)
        print("This is anotherDef1")
    def myDef1(self):
        print("myDef1 from anotherClass")

def main():
    with urllib.request.urlopen("http://www.google.com") as webURL:
         code = webURL.getcode()
         html = webURL.read()
         print(str(code)+" : "+str(html))
    # if path.exists("helloPython.txt") :
    #     src = path.realpath("helloPython.txt")
    #     head, tail = path.split(src)
    #     print("path: {p}\r\nfile: {f}".format(p=head, f=tail))
    #     dst = src + ".bak"
    #     shutil.copy(src, dst)
    #     shutil.copystat(src, dst)
    #     os.rename(dst, "bak"+tail)
    #     # shutil.make_archive("helloArchive", "zip", head)
    #     with ZipFile("helloPython.zip", "w") as myzip :
    #         myzip.write("helloPython.txt")
    #         myzip.write("bakhelloPython.txt")
    # print(os.name)
    # print("Item exists: " + str(path.exists("helloPython.txt")))
    # print("Item is a file: " + str(path.isfile("helloPython.txt")))
    # print("Item is a directory: " + str(path.isdir("helloPython.txt")))
    # print("Item's path: " + str(path.realpath("helloPython.txt")))
    # print("Item's path and name: " + str(path.split(path.realpath("helloPython.txt"))))
    # print("Today's date: {}".format(date.today()))
    # print("Today's format: {}".format(datetime.now().strftime("%A, %d, %B, %y")))
    # print("One year from now it will be: "+str(datetime.now() + timedelta(days=365)))
    # print(calendar.TextCalendar(calendar.SUNDAY).formatmonth(2017, 7, 0, 0))
    # f1 = open("helloPython.txt", "w+")
    # f1 = open("helloPython.txt", "a+")
    # for i in range(3):
    #     f1.write("This is line number %d\r\n"%(i+1))
    # f1.close()
    # f2 = open("helloPython.txt", "r")
    # # if f2.mode == 'r' :
    # #     print(f2.read())
    # for x in f2.readlines():
    #     print(x)
    # f2.close()
    # a = 5
    # print(a)
    # a = "World"
    # print("Hello "+str(a))
    # print(power(5, 9))
    # v = '7'
    # print(multi_add(3,int(v),67,78))
    # condition()
    # myVar = myClass()
    # myVar.myDef1()
    # yourValue1 = input("Enter your value : ");
    # myVar.myDef2(yourValue1)
    # anotherVar = anotherClass()
    # anotherVar.anotherDef1()
    # anotherVar.myDef1()
    # yourValue2 = input("Enter your value : ");
    # anotherVar.myDef2(yourValue2)

if __name__ == "__main__":
     main()
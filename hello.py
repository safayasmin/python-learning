# print("helo","world!")
# print("safa yasmin")
# print("hellooooo")
# print(35)


# print(3+3)
# print(10-3)

# print("hello safaa , are you 20 year old ?")

# x="python"
# y="is"
# z="simple"
# print(x+y+z)


# for x in "banana":
#     print(x)

# x=5
# print(type(x))

# x="hello safa"
# print(len(x))


# num=5
# x="good" if num>3 else "bad"
# print(x)


# for x in "banana":
#     print(x)


# x="safa "
# print(len(x))

# text="hello safa what are you doing"
# if "what" in text:
#     print("yes its in text")




# x="safa yasmin"
# print(x[-5:-2])

# x="safa Yasmin p."
# print(x.endswith("p."))


# age=17
# if age>18:
#     print("you are adult")

# print("you are minor")



# age=30

# if age>18:
#     print("you are greater than 18")

#     if age>21:
#         print("you are greater than 21")


# for i in range(4):
#     print(i)

# print("finished")

# def greet():
#     print("hello")
# greet()    

# count=0
# while count<=3:
#     print("count is greater than 0")
#     count+=1
# print("done")

# def add(a,b):
#     "find the sum of 2 nums"
#     return a+b
# print(add(1,2))
# print(add.__doc__)


# a=10
# b=20
# a,b=b,a
# print("a=",a)

# x={
#     "name":"safa",
#     "age":20
# }
# print(x["name"])


# age=18
# print(age<20 and age>16)



# mark=53
# if mark>60:
#     print("good")
# elif mark>50:
#     print("average")
# elif mark>40:
#     print("okey okey")
# else:
#     print("fail")


# day=5
# match day:
#     case 1:
#         print("sunday")
#     case 2:
#         print("monday")
#     case 3:
#         print("wednesday")
#     case _:
#          print("not daya")


# for i in range(4):
#     print("hello")



# x=["safa","shifa","sachu"]
# for item in x:
#     print(item)


# student={
#     "name":"safa",
#     "age":20
# }
# for value in student.values():
#     print(value)


# count=0
# while count<=5:
#     print(count)
#     count+=1


# for i in range(3):
#     print(i)
# else:
#     print("sytp")

# count=5
# while count>=1:
#     print("*" *count)
#     count-=1


# x=["safa","shifa","sachu"]
# i=0
# while i<len(x):
#     print(x[i])
#     i=i+1



# colors = ["Red", "Blue", "Green"]
# colors[1]="yellow"
# print(colors)

# numbers = [10, 20, 30]
# numbers.append(40)
# print(numbers)


# numbers = [10, 20, 30]
# numbers.insert(0,5)
# numbers.append(40)
# print(numbers)

# fruits = ["Apple", "Banana", "Mango", "Orange"]
# fruits.pop()
# print(fruits)

# x=[1,2,3,4,5]
# print(len(x))


# animals = ["Dog", "Cat", "Lion", "Tiger"]
# for i in animals:
#     print(i)

# x=[1,2,3,4,5]
# sum=0
# for i in x:
#     sum=sum+i
# print(sum)

# x=[4,5,2,9,1]
# x.sort(reverse=True)
# print(x)
# print(x[0])

# numbers=[1,4,3,7,8,9]
# num=int(input("enter number: "))
# if num in numbers:
#     print("found")
# else:
#     print("not found")


# numbers=(1,2,3)
# text=list(numbers)
# text[1]=33
# numbers=tuple(text)
# print(numbers)


# numbers=(1,2,2,3,4)
# print(numbers.count(3))


# colors={"red","white","pink"}
# colors.update(["blue","rose"])
# print(colors)


# a={1,2,3,4}
# b={3,4,5,6}
# print(a.difference(b))


# text=input("enter text")
# count=0
# for c in text.lower():
#     if c in "aeiou":
#         count+=1
# print("count is ",count)


# str="safa yasmin"
# print(str[::-1])


# text="madam"
# rev=text[::-1]
# if text==rev:
#     print("palindrom")
# else:
#     print("not palindrom")


# text="i love java python java"
# print(text.replace(" ",""))

# student={
#     "name":"safa",
#     "age":20
# }
# res=student.values()
# print(res)

# square = {x:x*x for x in range(1,6) if x%2==0}
# print(square)



# d = {}

# for i in range(5):
#     d[i] = i*i
# print(d)

# student={
#     "name":"safa",
#     "age":20
# }
# student.copy()
# print(student)


# student={
#     "Name"  : "Safa",
#     "Age"   : 19,
#     "Course" : "Python",
#     "Place"  : "Malappuram",
# }
# print(student["Name"])
# print(student["Course"])



# student = {
#     "Name": "Safa",
#     "Age": 19,
#     "Course": "Python",
#     "Place": "Malappuram"
# }
# student.update({"batch":20 ,"phone":"9876543210"})
# print(student)



# student = {
#     "Name": "Safa",
#     "Age": 19,
#     "Course": "Python",
#     "Place": "Malappuram"
# }
# student["Name"]="shahmaa"
# student["Course"]="mern"
# print(student)


# student = {
#     "Name": "Safa",
#     "Age": 19,
#     "Course": "Python",
#     "Place": "Malappuram",
#     "Phone": "9876543210"
# }
# student.pop("Phone")
# student.pop("Age")
# print(student)
# if "Name" in student:
#     print("found email")
# else:
#     print("not found")



# marks = {
#     "Safa": 95,
#     "Amina": 82,
#     "Rahul": 67,
#     "Arjun": 45,
#     "Fathima": 90
# }
# for name,mark in marks.items():
#     if mark>90:
#         print(name,"A")
#     elif mark>80:
#         print(name,"B")
#     elif mark>70:
#         print(name,"C")
#     elif mark>60:
#         print(name,"D")
#     else:
#         print(name,"Fail")


# text="python"
# print(text[::-1])


# text="Safa Yasmin"
# count=0
# for i in text:
#     if i.isupper():
#         count=count+1
# print(count)

# text="ShifaYasmin11@@"
# count=0
# for i in text:
#     if i.isalnum():
#         count=count+1
# print(count)    


# num=10
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
# print(sum)


# numbers = (1, 2, 3, 2, 4, 2, 5)
# result=numbers.count(2)
# print(result)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a|b)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a&b)




# def sum(a,b):
#     return a+b
# result=sum(2,3)
# print(result)

# x="globel"
# def outer():
#     x="enclosing"
#     def inner():
#         x="local"
#         print(x)
#     inner()
# outer()


# def student(name,age):
#     print(name)
#     print(age)
# student(age=20,name="safaa")

# def student(name="safaaa"):
#     print("hello ",name)
# student()

# def safa(*args):
#     print(args)
# safa(1,2,3,4,5)



# def sum(*args):
#     s=0
#     for i in args:
#         s=s+i
#     return s
# print(sum(1,2,3))

# def safa(**kwargs):
#     print(kwargs)
# safa(name="safaaa",age=20)


# def safa(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# safa(name="safaaa",age=20) 

# def safa(**args):
#     print(args)
# safa(id=1,name=2)


# def student(name,age):
#     print(name,age)

# data={
#     "name":"safaa",
#     "age":20
# }
# student(**data)

# def safa(n):
#     if n>5:
#         return
#     print(n)
#     safa(n+1)
# safa(1)

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))


# def fibonacci(n):
#     if n<=1:
#         return n

#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(6))



# add=lambda a,b:a+b
# print(add(10,20))

# print((lambda a,b:a+b)(10,30))

# print((lambda x:x*x)(2))



# mult=lambda a,b,c:a*b*c
# print(mult(1,2,3))

# numbers=[1,2,3,4]
# s=map(lambda x:x*x,numbers)
# print(list(s))

# x1=[1,2,3,4,6,8]
# print(list(filter(lambda x:x%2==0,x1)))


# students=[
# ("Safa",85),
# ("Rahul",90),
# ("Anu",70)
# ]
# students.sort(key=lambda x:x[1],reverse=True)
# print(students)


# from functools import reduce
# num=[1,2,3,4]
# sum=reduce(lambda a,b:a+b,num)
# print(sum)



# def outer(x):
#     return lambda y:x+y
# add=outer(5)
# print(add(10))

# try:
#     print(10/2)
# except ZeroDivisionError:
#     print("error")
# else:
#     print("sucsuss")
# finally:
#     print("helooo")

# def safa(numbers):
#     even=0
#     odd=0
#     for i in numbers:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     print(even)
#     print(odd)
# safa([1,2,3,4,5,6,7,8])


# def introduce(name, course="Python"):
#     print("hello ",name)
#     print("course",course)

# introduce("safa")

# def calculate(a, b):
#     return a+b,a-b,a*b
   
# print(calculate(10,20))

# def calculate(a, b):
#     sum=a+b
#     difference=a-b
#     multi=a*b
#     return sum,difference,multi
# s,d,m=calculate(10,20)
# print("sum",s)
# print("difference",d)
# print("multi",m)

# num=[10,20,30,40]
# squr=list(filter(lambda x:x>20 ,num))
# print(squr)


# num1=int(input("enter 1 num :"))
# num2=int(input("enter 2 num :"))

# try:
#     result=num1 / num2
#     print("result is ",result)

# except ZeroDivisionError:
#     print("zero come")



# def safe_divide(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("cannot divided by zero")
# print(safe_divide(10,2))
    
# def sum_n(n):
#    if n==1:
#       return 1
#    return n+sum_n(n-1)
# print(sum_n(10))

# class student:
#     pass
# s1=student()
# s1.name="safa"
# s1.age=20
# print(s1.name)
# print(s1.age)

# class student:
#     def greet(self):
#         print("helloooo")
# s1=student()
# s1.greet()

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# s1=student("safa",20)
# print(s1.name)
# print(s1.age)

# class student:
#     pass
#     print("helloo")
# s1=student()
# print(student)


# class student:
#     def greet(self):
#         self.name="safaa"
#         print(self.name)

# s1=student()
# s1.greet()

# class student:
#     def __init__(self):
#         self.name="safa"
# s1=student()
# print(s1.name)


# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student("safaa",20)
# print(s1.name)
# print(s1.age)


# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student("safaa",29)
# s2=student("ashmil",20)
# s1.name="shofaaaa"
# print(s1.name)
# print(s2.name)

# class student:
#     school="ABC SCHOOL"
    
#     def __init__(self,name):
#         self.name=name
# student.school="abcd"  
# s1=student("safa")
# s2=student("sachu")

# print(s1.school)
# print(s2.school)


# class student:
#     school="abx"
#     @classmethod
#     def change(cls,newname):
#         cls.school=newname

# student.change("hfffff")
# print(student.school)


# class student:
#     school="abx"
#     @classmethod
#     def changeclass(cls,newschool):
#         cls.school=newschool
# student.school="abdhg"
# print(student.school)

# class car:
#     brand="bmw"
#     @classmethod
#     def show_brand(cls):
#         print(cls.brand)

# car.show_brand()
    


# class Employee:
#     company="Google"
#     @classmethod
#     def change_company(cls,newcmpy):
#         cls.company=newcmpy
# Employee.company="Microsoft"
# print(Employee.company)


# class clacolator:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(clacolator.add(3,5))

# class student:
#     @staticmethod
#     def greet():
#         print("hello safa")
# student.greet()


# class student:
#     @staticmethod
#     def checkage(age):
#         if age>18:
#             print("adult")
#         else :
#             print("minor")

# student.checkage(2)


# class student:
#     @staticmethod
#     def hello():
#         print("hello safaaa")
# s1=student()
# s1.hello()



# class animal:
#     def eating(self):
#         print("eating")
# class dog(animal):
#     pass
# class cat(animal):
#     pass

# s1=animal()
# s1.eating()

# class Animal:
#     def eating(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog()

# d.eating()
# d.bark()


# class animal:
#     def eat(self):
#         print("hello safaa")
# class dog(animal):
#     print("koooiii")
#     pass 
# d=dog()
# d.eat()


# class Parent:
#     def introduce(self):
#         print("i am person")
# class Student(Parent):
#     pass

# s1=Student()
# s1.introduce()


# class Father:
#     def fat(self):
#         print("i am father")

# class Mother:
#     def mat(self):
#         print("i am mother")

# class Child(Father,Mother):
#     pass
# c=Child()
# c.mat()
# c.fat()
    

# class Grandparant:
#     def grand(self):
#         print("i am grandparant")
# class Parant(Grandparant):
#     def para(self):
#         print("i am parant")
# class Child(Parant):
#     def chi(self):
#         print("i am child")
# c=Child()
# c.grand()
# c.para()
# c.chi()


# class Animal:
#     def eat(self):
#         print("eating start")


# class dog(Animal):
#     pass
# class cat(Animal):
#     pass
# class tiger(Animal):
#     pass
# t=tiger()
# t.eat()
# d=dog()
# d.eat()



# class Parent:
#     def par(self):
#         print("hello safaa")
# class Child(Parent):
#     def par(self):
#         super().par()
#         print("koiiiiiiii")
# c=Child()
# c.par()
    


# class parant:
#     def __init__(self,name):
#         self.name=name

# class chlid(parant):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age

# ch=chlid("safaa",29)
# print(ch.name)
# print(ch.age)


# class animal:
#     def dog(self):
#         print("it is dog")

# class cat(animal):
#     pass

# d=cat()
# d.dog()


# class Animal:
#     def ani(self):
#         print("hello safaaa")
# class Dog(Animal):
#     pass
# d=Dog()
# print(isinstance(d,Dog))
# print(issubclass(Dog,Animal))



# class Student:
#     def safa(self,name,age):
#         self.name=name
#         self.age=age
# s=Student()
# s.safa("safa",20)
# print(s.name)
# print(s.age)


# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display(self):
#         print("brand",self.brand)
#         print("model",self.model)
# c=car("bmw","supra")
# c.display()


# class bankaccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print(amount,"deposite sucsuss")
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance=self.balance-amount
#             print(amount,"withdrow sucsuss")
#         else:
#             print("error")

#     def display_balance(self):
#        print("Account Holder:", self.account_holder)
#        print("Current Balance:", self.balance)

# b1 = bankaccount("Safa", 1000)

# b1.display_balance()

# b1.deposit(500)

# b1.withdraw(300)

# b1.display_balance()



# class demo:
#     def add(self,a,b=0):
#         print(a+b)

# d=demo()
# d.add(10)
# d.add(20,30)


# class demo:
#     def add(self,*args):
#         print(sum(args))
# d=demo()
# d.add(10,29)
# d.add(1,2,4,35,7)


# class demo:
#     def add(self,**kwargs):
#         print(kwargs)

# d=demo()
# d.add(name="safaa",age=20)



# class bankaccount:
#     def __init__(self):
#         self._balance=10000
#     def deposit(self,amount):
#         self._balance=self._balance+amount
#     def total(self):
#         print("balance",self._balance)
# b=bankaccount()
# b.deposit(3000)
# b.total()

# class bankacc:
#     def __init__(self):
#         self.__balance=10000
    
# b=bankacc()
# print(b.__init__())


# class student:
#     def __init__(self):
#         self.__mark=40
#     def set__marks(self,marks):
#         self.__mark=marks
#     def get__marks(self):
#         return self.__mark
# s=student()
# s.set__marks(50)
# print(s.get__marks())
        

# from abc import ABC, abstractmethod

# class animal(ABC):
#     @abstractmethod
#     def dog(self):
#         print("hellooooo")
# class safa(animal):
#     def dog(self):
#         print("koi")
# a=safa()
# a.dog()


# nums = [10, 20, 30]

# it = iter(nums)

# print(it)

# nums = [10, 20, 30]

# it=iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))


# def show():
#     yield 10
# g=show()
# print(next(g))


# num=[1,2,3,4]
# def squar(x):
#     return x*x
# res=map(squar,num)
# print(list(res))


# num=[1,2,3,4]
# res=map(lambda x:x*x ,num)
# print(list(res))


# names = ["safa", "python", "java"]
# res=[]
# for i in names:
#     res.append(i.upper())
# print(res)

# names = ["safa", "python", "java"]
# res=map(str.upper ,names)
# print(list(res))


# salary = [20000, 30000, 40000]
# result=map(lambda x:x+5000 ,salary)
# print(list(result))


# num=[10,23,3,44,45,60]
# res=filter(lambda x:x%2==0 ,num)
# print(list(num))


# names = ["Ali", "Safa", "Python", "AI"]
# res=filter(lambda x:len(x)>=4 ,names)
# print(list(res))


# marks = [35, 80, 25, 90, 40]
# passed=filter(lambda x:x>=28 ,marks)
# print(list(passed))


# from functools import reduce
# num=[1,2,3,4,5]
# res=reduce(lambda x,y:x+y ,num)
# print(res)


# from functools import reduce
# num=[1,2,3,4,9,6,5]
# res=reduce(lambda x,y:x if x>y else y ,num)
# print(res)

# names = ["Safa", "Ali", "Sara"]
# marks = [90, 80, 95,3]
# res=zip(names,marks)
# print(list(res))


# names = ["Safa", "Ali", "Sara"]
# marks = [90, 80, 95,3]
# for name,mark in zip(names,marks):
#     print(name,mark)




# def outer():
#     message="helloo"
#     def inner():
#         print(message)
#     return inner
# dev=outer()
# dev()


# def hello():
#     print("hello11")
# x=hello
# x()


# def hello():
#     print("kooiiii")
# def display(fun):
#     fun()
# display(hello)



# def decorator(fun):
#     def wraper():
#         print("before codeee")

#         fun()
#         print("after function")
    
#     return wraper
# @decorator
# def hello():
#     print("hellooooo")
# hello()



# def decorator(fun):
#     def wraper(*args):
#         print("1111111")
#         fun(*args)
#         print("2222222222")
#     return wraper
# @decorator
# def hello(name,age):
#     print(f"my name is {name} ,my age is {age}")
# hello("safa",20)


# def decorator(fun):
#     def wraper(**kwargs):
#         print("koiii")
#         fun(**kwargs)
#         print("byyy")
#     return wraper
# @decorator
# def sum(name,age,place):
#     print(name,age,place)
# sum(name="safaa",age=20,place="koramkode")


# class student:
#     def __str__(self):
#         return "hellooo"
# s=student()
# print(s)


# class student:
#     def __init__(self,name):
#         self.name=name
#         print(self.name)

# s=student("safffa")

# class student:
#     def __init__(self,num):
#         self.num=num
#     def __add__(self,value):
#         return self.num+value.num
# s1=student(20)
# s2=student(10)
# print(s1+s2)


# class student:
#     def __add__(self,a,b):
#         return a+b

# s1=student()
# print(s1.__add__(10,20))


# class student:
#     def __len__(self):
#         return 1000
# s=student()
# print(len(s))
    

# class student:
#     def __init__(self,age):
#         self.age=age
#     def __eq__(self,other):
#         return self.age==other.age
# s=student(20)
# s2=student(20)
# print(s==s2)


# def change(nums):
#     nums.append(40)
#     return nums
# print(change([1,2,3,4]))


# def message():
#     return 10
# val=message()
# print(val)

# def message(name):
#     print("heloo",name)
# message("safa")
   


# def add(a,b):
#     return a+b
# print(add(10,20))

# def square(a):
#     return a*a
# print(square(5))



# class student:
#     def safa(self):
#         print("hello safaaa")
# def shifa(self):
#     print("koiiiii")
# student.safa=shifa

# s=student()
# s.safa()


# num=11
# for i in range(2,num):
#     if num%i==0:
#         print("not a prime")
#         break
# else:
#         print("prime")


 

# num=[1,4,2,5,3,8,9]
# for number in num:
#     if number<=1:
#         print(number ,"not a prime")
#         continue
#     for i in range(2,number):
#         if number%i==0:
#             print(number ,"not prime")
#             break
#     else:
#         print(number, "prime")



# def safa(n):
#     if(n<=1):
#         return 1
#     else:
#         return n+safa(n-1)
# print(safa(10))
     












# import math
# print(math.sqrt(25))

# age=20
# if age>=18:
#     print("safaaaa")

#     if age<=20:
#         print("sjkkkk")


# count=0
# while count<=3:
#     print(count)
#     count=count+1
# print("done")

# a=b=c=100
# print(a,b,c)


# a=100
# b=200
# a,b=b,a
# print(a)

# name=input("enter your name")
# print(name)



# num=[1,2,3,4]
# for i in num:
#     print(i)


# student={
#     "name":"safaa",
#     "age":20
# }
# print(student["name"])

# age="20"
# print(int(age)+10)


# a = [10, 20, 30]
# b = a
# b.append(40)
# print(a)
# print(b)


# a = [10, 20, 30]
# b = a.copy()
# b.append(40)
# print(a)
# print(b)


# a = "Python"
# b = a
# b += " Programming"
# print(a)
# print(b)


# list1 = [10,20,30]
# list2=list1
# list2.append(40)
# for i in list1:
#     print(i)
# for i in list2:
#     print(i)

# list1 = [1, 2, 3]
# list2 = list1

# print(id(list1) == id(list2))

# list2 = [1, 2, 3]

# print(id(list1) == id(list2))

# a = (10, 20, [30, 40])
# a[2].append(50)
# print(a)


# a = (10, 20, [30, 40])
# a[2] = [50, 60]
# print(a)

# str="madam1"
# r=str[::-1]
# if str==r:
#     print("palindrom")
# else:
#     print("not palindrom")



# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique=list(set(numbers))
# print(unique)

# numbers = [10,67,45, 23, 67, 12]
# numbers.sort(reverse=True)
# if numbers[0]==numbers[1]:
#     print(numbers[2])
# else:
#     print(numbers[1])


# numbers = [1, 2, 3, 4, 5]
# square=[n*n for n in numbers]
# print(square)


# numbers = [[1, 2], [3, 4], [5, 6]]
# for group in numbers:
#     for i in group:
#         print(i)


# student = ("Safa", 19, "Python")
# name,age,course=student
# print("name is :",name)
# print("age is :",age)
# print("course is :",course)

# data = (10, (20, 30), (40, 50))
# print(data[1][1])
# print(data[2][1])


# a={1,2,3,4}
# b={1,2,3,4,5,6,7}
# print(a.issubset(b))

# numbers = [1, 2, 2, 3, 3, 4, 5, 5]
# print(set(numbers))


# students_python = {"Safa", "Amina", "Rahul", "Arjun"}
# students_java = {"Rahul", "Arjun", "Fathima"}
# print(students_python.intersection(students_java))


# numbers = [10, 20, 30, 40]
# print(tuple(numbers))


# a = [1, 2, 3]
# b = a
# c = a.copy()
# b.append(4)
# c.append(5)
# print(a)
# print(b)
# print(c)


# a = [1, 2, 3]
# b = a
# a += [4]
# print(a)
# print(b)


# a = [1, 2, [3, 4]]
# b = a.copy()
# b[2].append(5)

# print(a)
# print(b)

# a = [10, 20, [30, 40]]
# b = a.copy()

# b[2].append(50)

# print(a)
# print(b)

# numbers = [10, 20, 30, 40, 50, 60]
# a = numbers[1:5]
# b = a[::-1]
# print(a)
# print(b)


# student = {
#     "name": "Safa",
#     "age": 19,
#     "course": "Python",
#     "marks": 90
# }
# student.fromkeys(["name","place"],None)
# print(student)


# text="Safa yaasmin puu"
# res=text.split(" ")
# print(res)
# s=" ".join(res)
# print(s)

# text="python is very easy"
# res=text.find("very1")
# print(res)


# text="safa yasmin"
# res=text.count("a")
# print(res)

# text="safa yasmin"
# res=text.endswith("saf11")
# print(res)



# student = {
#     "name": "Safa",
#     "age": 19,
#     "course": "Python",
#     "marks": 95
# }
# print(student.keys())
# print(student.values())
# print(student.get("email"))
# student.update({"place":"malappuram"})
# student.update({"marks":98})
# student.pop("age")
# print(student.items())


# marks = {
#     "Safa": 95,
#     "Amina": 82,
#     "Rahul": 67,
#     "Arjun": 45,
#     "Fathima": 90
# }
# for name,score in marks.items():
#     if score>=80:
#         print(name ,score)


# student = {
#     "name": "Safa",
#     "age": 19,
#     "course": "Python",
#     "marks": 95,
#     "place": "Malappuram",
#     "email":"safa@gmail.com"
# }

# print(len(student))
# if "email" in student:
#     print(student["email"])
# else:
#     print("not email")


# student = {
#     "name": "Safa",
#     "age": 19,
#     "course": "Python",
#     "marks": 95
# }
# student.update({"place": "Malappuram"})
# student.update({"phone": "9876543210"})
# student.update({"marks":98})
# student.pop("age")
# for key,value in student.items():
#     print(key,value)



# student = {
#     "name": "Safa Yasmin",
#     "course": "Python Programming",
#     "place": "malappuram"
# }
# print("name is ", student["name"].upper())
# print(student["course"].lower())
# print(student["place"].capitalize())
# print(len(student["name"]))
# print(student["course"].startswith("Python"))
# print(student["course"].replace("Programming","Development"))


# text = "Python is easy and Python is powerful"
# print(text.count("Python"))
# print(text.index("Python"))
# print(text.replace("Python","java"))
# print(text.split())
# print(text.endswith("powerful"))


# text = "Python Programming"
# count=0
# consonent=0
# for i in text:
#     if i in "aeiou":
#         count=count+1
#     else:
#         consonent=consonent+1
# print(count)
# print(consonent)
# print(text.replace(" ",""))



# text = "  Python Programming  "
# print(text.strip())
# print(text.upper())
# print(text.title())
# print(text.find("Program"))
# print(text.count("m"))
# print(text.startswith("Python"))


# text = "python123"
# print(text.islower())


# students = {
#     "s1": "Safa Yasmin",
#     "s2": "Amina",
#     "s3": "Rahul",
#     "s4": "Fathima"
# }

# for name in students.values():
#     if len(name)>5:
#         print(name)


# text = "Python Python Java Python"
# words = text.split()
# print(words)
# print(len(words))
# print(words.count("Python"))
# print(words.index("Java"))


# def greet(name):
#     print("hello",name)
#     print("welcome to python")
# greet("safa")

# def calculate_sum(a,b):
#    return a+b
# print(calculate_sum(10,20))

# def greet(name, message="Welcome to Python"):
#    print("hello",name)
#    print(message)
# greet("safa")


# def calculate(*args):
#     total=0
#     for num in args:
#         total += num
#     print("sum is",total)
    
# calculate(10,20,30)

# text="safa yasmin hello"
# res=text.split()

# for str in res:
#     print(str[::-1])


# def student_info(**kwargs):
#     for key,val in kwargs.items():
#         print(key ,":",val)

# student_info(
#     name="safa",
#     age=19,
#     course="python"
# ) 

# a=[1,2]
# b=a
# print(a is b)

# fruits = ["apple", "banana", "mango", "orange"]

# print("mango" in fruits)
# print("grape" in fruits)

# numbers = [10, 20, 30, 40, 50]

# print(25 not in numbers)
# print(30 not in numbers)

# a = [10, 20, 30]
# b = a
# c = [10, 20, 30]
# print(20 in a)
# print(40 in b)
# print(a is b)
# print(a is c)


# a = [10, 20, [30, 40]]
# b = a
# c = a.copy()
# print(30 in a)
# print([30, 40] in a)
# print(a is b)
# print(a is c)
# print(a[1] is c[1])


# text="malayalam"
# res=text[::-1]
# if text==res:
#     print("its a palindrom")
# else:
#     print("not a palindrom")


# def student(*args, **kwargs):
#     print(args,kwargs)
# student(
#     "Python",
#     "JavaScript",
#     name="Safa",
#     age=19
# )


# def factorial(n):
#     if n==1:
#         return 1
#     return n+factorial(n-1)
# print(factorial(10))



# def power(a, b):
#     if b == 0:
#         return 1
#     return a ** b
# print(power(2, 5))


# def fabonacci(n):
#     if n<=1:
#         return n
#     return fabonacci(n-1)+fabonacci(n-2)
# print(fabonacci(10))


# num=123
# res=str(num)
# revers=res[::-1]
# print(int(revers))


# larger=lambda x,y:x if x>y else y
# print(larger(10,20))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list(filter(lambda x:x%2==0 ,numbers)))

# numbers = [1, 2, 3, 4, 5]
# print(list(map(lambda x :x*x ,numbers)))


# marks = {
#     "Safa": 95,
#     "Amina": 72,
#     "Rahul": 88,
#     "Arjun": 45
# }
# print(list(filter(lambda x:x[1]>=80 ,marks.items())))


# def greet(name):
#     print("function started")
#     print(f"hello {name}")
# greet("safa")



# try:
#     num1=int(input("enter first num :"))
#     num2=int(input("enter first num2 :"))

#     result=num1/num2

#     print("result :",result)
# except ZeroDivisionError:
#     print("cannot devided by zero")
# finally:
#     print("helo safa")


class student:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
s=student(10,20)
print(s.sum())
        


    


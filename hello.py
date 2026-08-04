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


def fibonacci(n):
    if n<=1:
        return n

    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))




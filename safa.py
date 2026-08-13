# class Father:
#     def sound(self):
#         print("hellooo father")
# class Mother:
#     def sound(self):
#         print("hello mother")
# class Child(Father,Mother):
#     pass
# c=Child()
# c.sound()



# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# res=set(a)&set(b)
# print(list(res))


# names = ["Safa", "Shifa", "Amina"]
# marks = [95, 88, 92]
# res=zip(names,marks)
# print(dict(res))



# marks = {
#     "Safa": 95,
#     "Shifa": 88,
#     "Amina": 92,
#     "Rahul": 70
# }
# res=dict(filter(lambda x:x[1]>80 ,marks.items()))
# print(res)


# numbers = [10, 15, 20, 25, 30, 35]
# numbers.insert(1,99)
# print(list(numbers))


# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)


# a = [[10, 20], [30, 40]]
# b = a.copy()
# # Outer list change
# b.append([50, 60])
# print(a)
# print(b)


# a = [[10, 20], [30, 40]]
# b = a.copy()
# b[0].append(99)
# print(a)
# print(b)

# s={1,2,3}
# b={3,4,5}
# print(s.intersection(b))



# class Animal:
#     def sound(self):
#         print("hello safaaa")
# def koi(self):
#     print("kooiiii")
# Animal.sound=koi
# a=Animal()
# a.sound()  


# def Number():
#     yield 1
#     yield 2
#     yield 3
# g=Number()
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration:
#     print("error")


# num=10
# if num<=1:
#     print("not a prime")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("not a prime")
#             break
#     else:
#         print("prime")   


# def decorator(fun):
#     def wraper(a,b):
#         fun(10,20)
#         print(a*b)
#         print("kooiii")
#     return wraper
# def helloo(a,b):
#     print("sagffaaa")
#     print(a+b)
# helloo(10,10)



student = {
    "name": "Safa",
    "age": 20,
    "mark": 5,
    "city": "Malappuram"
}
if student["mark"]>80:
    print(student)




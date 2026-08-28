# numbers=[1,2,3,4]
# for x in numbers:
#     if x==3:
#         print("found")
#     else:
#         print(x)



# numbers = [10, 20, 30, 40]
# numbers.append(50)
# print(numbers)
# numbers.remove(10)
# print(numbers)



# linked list eg

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# # Nodes create cheyyunnu
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# # Nodes connect cheyyunnu
# node1.next = node2
# node2.next = node3
# node3.next=node4

# # Print
# current = node1

# while current:
#     print(current.data)
#     current = current.next





# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.next=node3

# head1=node1
# def reverse(head):
#     prev = None
#     current = head

#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
#     return prev

# head2 = reverse(head1)
# current = head2
# while current:
#     print(current.data)
#     current = current.next



# def findmminmax(num):
#     max=num[0]
#     min=num[0]
#     for i in num:
#         if i>max:
#             max=i

#         if i<min:
#             min=i
#     return max,min
# print(findmminmax([2,7,8,5,0,9,10]))




# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.next=node3


# current=node1
# while current:
#     print(current.data)
#     current=current.next




# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.prev=node1

# node2.next=node3
# node3.prev=node2

# newnode=Node(25)

# newnode.prev=node2
# newnode.next=node3

# node2.next=newnode
# node3.prev=newnode

# current=node1
# while current:
#     print(current.data)
#     current=current.next


    


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.next=node3


# head=node1
# current=head
# target=30
# while current.next:
#     if current.next.data==target:
#         current.next=current.next.next
#         break
#     current=current.next
# current=head
# while current:
#     print(current.data)
#     current=current.next




# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.next=node3


# head=node1
# prev=None
# current=head
# while current:
#     next_node=current.next
#     current.next=prev
#     prev=current
#     current=next_node
# head=prev

# current=head
# while current:
#     print(current.data)
#     current=current.next



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.next=node3


# head=node1

# newnode=Node(40)
# newnode.next=node2.next
# node2.next=newnode

# current=head
# while current:
#     print(current.data)
#     current=current.next





# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None


# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)

# node1.next = node2
# node2.prev = node1

# node2.next = node3
# node3.prev = node2

# node3.next = node4
# node4.prev = node3

# node4.next = node5
# node5.prev = node4

# newnode = Node(88)

# newnode.next = node3.next
# newnode.prev = node3

# node3.next.prev=newnode
# node3.next=newnode

# current=node1
# while current:
#     print(current.data)
#     current=current.next



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def list_to_linkedlist(values):
#     if not values:
#         return None

#     head=Node(values[0])
#     current=head

#     for value in values[1::]:
#         newnode=Node(value)

#         current.next=newnode
#         current=newnode

#     return head
# values=[1,2,3,4,5]
# head=list_to_linkedlist(values)

# current=head
# while current:
#     print(current.data)
#     current=current.next



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.next=node3
# head=node1

# def linkedlist_to_list(head):
#     result=[]
#     current=head
#     while current:
#         result.append(current.data)
#         current=current.next
#     return result

# res=linkedlist_to_list(head)
# print(res)


# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print("stack is ",stack)
# remove=stack.pop()
# print("remove is ",remove)
# print("stack ",stack)
# #peek
# print("top element",stack[-1])




# stack using list

# stack=[]
# stack.append(10)
# stack.append(20)
# print(stack)
# print(stack[-1])
# print(len(stack))






# # stack single linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# top=None
# newnode=Node(10)
# newnode.next=top
# top=newnode

# newnode=Node(20)
# newnode.next=top
# top=newnode

# newnode=Node(30)
# newnode.next=top
# top=newnode

# if top is None:
#     print("list is empty")
# # pop and peek 
# else:
#     top=top.next
#     print("peek is ",top.data)

# count=0
# current=top
# while current:
#     count+=1
#     print(current.data)
#     current=current.next
#     print("count is :",count)







# # stack in double linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# top=None
# newnode=Node(10)
# newnode.next=top
# newnode.prev=None

# if top is not None:
#     top.prev=newnode
# top=newnode

# newnode=Node(20)
# newnode.next=top
# newnode.prev=None
# if top is not None:
#     top.prev=newnode
# top=newnode

# newnode=Node(30)
# newnode.next=top
# newnode.prev=None

# if top is not None:
#     top.prev=newnode
# top=newnode

# if top is None:
#     print("empty list")
# else:
#     print("remove is ",top.data)
#     top=top.next

# if top is None:
#     print("stack list is empty")
# else:
#     print("stack is :",top.data)

# current=top
# while current:
#     print(current.data)
#     current=current.next





# # reverse a string useing stack

# name="safa"
# stack=[]
# for char in name:
#     stack.append(char)

# reverse=""
# while stack:
#     reverse+=stack.pop()
# print(reverse)



# # valid paranthasis using stack

# def is_valid(s):
#     stack = []

#     pairs = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
#     for char in s:
#         if char in "({[":
#             stack.append(char)
#         else:
#             if not stack:
#                 return False
#             if stack[-1]==pairs[char]:
#                 return True
#             stack.pop()
#     return len(stack)==0
# print(is_valid("({})"))




# # queue

# queue = []
# # Enqueue
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# # Peek
# print("Front:", queue[0])
# # Dequeue
# item = queue.pop(0)
# print("Removed:", item)
# print(queue)




# ithan standard queue karanam nokkuka

# from collections import deque
# queue=deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue[0])
# print(queue.popleft())
# print(queue)



# # queue using single linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# front=None
# rear=None

# newnode=Node(10)
# if rear is None:
#     front=newnode
#     rear=newnode
# else:
#     rear.next=newnode
#     rear=newnode

# newnode=Node(20)
# if rear is None:
#     front=newnode
#     rear=newnode
# else:
#     rear.next=newnode
#     rear=newnode

# newnode=Node(30)
# if rear is None:
#     front=newnode
#     rear=newnode
# else:
#     rear.next=newnode
#     rear=newnode

# if front is None:
#     print("no data")
# else:
#     print("pop element is :",front.data)
#     front=front.




# if front is None:
#     print("not a list")
# else:
#     print("peek value is :",front.data)
# current=front
# while current:
#     print(current.data)
#     current=current.next

    


# queue using double linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# front=None
# rear=None

# newnode=Node(10)
# if front is None:
#     front=newnode
#     rear=newnode
# else:
#     rear.next=newnode
#     newnode.prev=rear
#     rear=newnode

# newnode=Node(20)
# if front is None:
#     front=newnode
#     rear=newnode
# else:
#     rear.next=newnode
#     newnode.prev=rear
#     rear=newnode

# newnode=Node(30)
# if front is None:
#     front=newnode
#     rear=newnode
# else:
#     rear.next=newnode
#     newnode.prev=rear
#     rear=newnode

# if front is None:
#     print("no list")
# else:
#     print("remove data is :",front.data)
#     front=front.next

#     if front is not None:
#         front.prev=None


# if front is None:
#     print("no list")
# else:
#     print("peek data is :",front.data)

# count=0
# current=front

# while current:
#     count+=1
#     print(current.data)
#     current=current.next
# print("count is :",count)




# reverese a queue

# queue=[1,2,3]
# stack=[]
# while queue:
#     stack.append(queue.pop(0))
# while stack:
#     queue.append(stack.pop())
# print(queue)





# from collections import deque
# queue=deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue[0])
# print(queue.popleft())
# print(queue)
# queue.append(40)
# print(queue)




# circular queue eg

# queue = [None] * 3

# front = 0
# rear = -1
# size = 3

# # Enqueue 10
# rear = (rear + 1) % size
# queue[rear] = 10

# # Enqueue 20
# rear = (rear + 1) % size
# queue[rear] = 20

# # Enqueue 30
# rear = (rear + 1) % size
# queue[rear] = 30

# print(queue)

# # Dequeue 10
# print("Removed:", queue[front])
# print("peek is :",queue[front])

# queue[front] = None
# front = (front + 1) % size

# print(queue)
# # Enqueue 40
# rear = (rear + 1) % size
# queue[rear] = 40
# print(queue)



# from collections import deque
# queue=deque([10,20])
# queue.popleft()
# print(queue)



arr=[10,20,30,40,5,6]
target=30
for i in range(len(arr)):
    if arr[i]==target:
        print("found the value :",i)
        break
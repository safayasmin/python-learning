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


stack=[]
stack.append(10)
stack.append(20)
print(stack)
print(stack[-1])
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



def findmminmax(num):
    max=num[0]
    min=num[0]
    for i in num:
        if i>max:
            max=i

        if i<min:
            min=i
    return max,min
print(findmminmax([2,7,8,5,0,9,10]))
    

    
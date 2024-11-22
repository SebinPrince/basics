'''AUTHOR=SEBIN PRINCE
DESCRIPTION:Input two lists and merge it in other list all even number occur first followed by odd numbers.both even numbers and odd numbers should be in sorted order
'''
list_1=[1,6,4,8,3]
print("list1",list_1)
list_2=[4,7,2,9,0]
print("list2",list_2)
merged=list_1+list_2
print("Merged list=",merged)
even_list=[]
odd_list=[]
for i in merged:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
d=even_list+odd_list
print("Sorted order",d)

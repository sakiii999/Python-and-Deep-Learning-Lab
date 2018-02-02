sentence=input("Please enter the sentence: ")
list1=sentence.split()
var1=len(list1)
# If the input list is even,then the below if block is executed
if(var1%2==0):
    x=var1/2
    y=int(x-1)
    print(list1[y]+" "+list1[y+1])
# If the input list length is odd,then the below else block is executed
else:
    x=int(var1/2)
    print(list1[x])
# List is sorted in increasing order of their respective length
sortedwords=sorted(list1, key=len)
# Longest word is printed after sorting
print(sortedwords[-1])
list2=[]
var2=len(list1)
y=0
# The given sentenced is reversed and appended to the new list
for x in range(var2):
    list2.append(list1[y][::-1])
    y=y+1
print(list2)
books={"python":50,"web":30,"c":20,"java":40}
finallist=[]
#The starting and ending numbers for the range are taken from user input
start=int(input("Please enter the start number: "))
end=int(input("Please enter the end number: "))
#To iterate inside the dictionary items
for key,value in books.items():
    #The loop is executed if start and end values are equal or greater than the given value
    if value >= start and value <= end:
        #The result are appended to the final list
        finallist.append(key)
#Converts the list to string for the desired output
str1=','.join(finallist)
print("You can purchase these books ("+str1+")")
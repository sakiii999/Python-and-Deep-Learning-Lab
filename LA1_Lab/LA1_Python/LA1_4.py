webapp=['Saketh','Pujitha','Sravani','Veda'] # Webapplication Student List
python=['Saketh','Pujitha','Sudheesha','Namrata','Sarat'] # Python List
var1=len(webapp)
var2=len(python)
x=0
same_list=[]
diff_list=[]
for i in range(var1):
    if webapp[x] in python: # Compares webapp student list to python student list
        same_list.append(webapp[x]) # The students registered for both classes are added to this list
    else:
        diff_list.append(webapp[x]) # The students registered only for single class are added to this list
    x=x+1
y=0
for j in range(var2): # Compares python student list to webapp student list
    if python[y] not in webapp:
        diff_list.append(python[y]) # The students registered only for single class are added to this list
    y=y+1
print(same_list)
print(diff_list)

Contact_list=[{"name":"Saketh","number":"1234","email":"sakethgaruda@gmail.com"},{"name":"Sarat","number":"5678","email":"tracesarat@gmail.com"}]
#While loop is used to prompt the menu options until user exits program
while True:
    print("a) Display contact by name")
    print("b) Display contact by number")
    print("c) Edit contact by name")
    print("d) Exit")

    userinput=str(input("Please enter your choice: "))
    #If user enters option 'a' then the below loop is executed
    if userinput=='a':
        input1=(input("Please enter the name: "))
        #Compares the given user input to the dictionary keys for output
        print(next(item for item in Contact_list if item["name"]==input1))
    elif userinput=='b':
        input2=(input("Please enter the number: "))
        # Compares the given user input to the dictionary keys for output
        print(next(item for item in Contact_list if item["number"]==input2))
    elif userinput=='c':
        input3=input("Please enter the contact name you want to edit: ")
        # Compares the given user input to the dictionary keys for output
        for item in Contact_list:
            if item["name"]==input3:
                # The given dictionary is updated with the user input
                item["number"]=input("Please enter the new contact number: ")
        print(Contact_list)
    elif userinput=='d':
        break






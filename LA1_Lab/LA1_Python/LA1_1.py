password=input("Please enter the password: ")
#Special characters are stored in a list
special_char=['$','@','!','*']
for i in password:
    # If the given password is less than 6 and greater than 16,the loop is executed and breaks thereafter
    if 6>len(password)<16:
        print("The password length should be in range 6-16 characters")
        break
    # If the given password does not have a digit,the loop is executed and breaks thereafter
    elif not any(x.isdigit() for x in password):
        print("Should have atleast one number")
        break
    # If the given password does not have special character,the loop is executed and breaks thereafter
    elif not any(x in special_char for x in password):
        print("Should have special character")
        break
    # Given password is validated for atleast one uppercase character,is not present the loop is executed and breaks thereafter
    elif not any(x.isupper() for x in password):
        print("Should have atleast one uppercase character")
        break
    # Given password is validated for atleast one lowercase character,is not present the loop is executed and breaks thereafter
    elif not any(x.islower() for x in password):
        print("Should have atleast one lowercase character")
        break
    # Loop is executed if and only password meets all rules
    else:
        print("Password Accepted by meeting all rules")
        break



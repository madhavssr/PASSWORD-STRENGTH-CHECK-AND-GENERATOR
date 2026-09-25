def strength_report(result1,result2):                                          #Accessing result 1 and result 2 from length check and character variation check respectively. 
    if result1==result2==True:
        print("\nYour Password is Secure")
    
    elif result1==True and result2==False:
        print("\nYour password needs atleast one capital letter,special character and number")
        print("\nYour password is not secure.")
    
    elif result1==False and result2==True:
        print("\nYour password needs to be atleast 8 characters long.")
        print("\nYour password is not secure.")
    
    else:
        print("\nYour password needs atleast one capital letter,special character and number")
        print("Your password needs to be atleast 8 characters long.")
        print("\nYour password is not secure.")
        

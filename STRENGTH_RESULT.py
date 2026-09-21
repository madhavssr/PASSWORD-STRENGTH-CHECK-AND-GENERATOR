def strength_report(result1,result2):
    if result1==result2==True:
        print("Your Password is Secure")
    elif result1==True and result2==False:
        print("Your password needs atleast one capital letter,special character and number")
    elif result2==False and result2==True:
        print("Your password needs to be atleast 8 characters long.")
    else:
        print("\nYour password needs atleast one capital letter,special character and number")
        print("Your password needs to be atleast 8 characters long.")
        

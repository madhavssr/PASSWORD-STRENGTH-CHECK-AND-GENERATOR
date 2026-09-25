import random
import string

def password_generator():
    while True:
        
        try:                                                                   #Error Handling 
            l = int(input("\nEnter length of required password: "))            #Accepting length of required password
            if l < 8:
                raise ValueError("Length must be at least 8.")
            break
        except ValueError:                                                     #Value Error Handled 
            print("Invalid input. Please enter a whole number (8 or more).")

    ch = string.ascii_letters + string.digits + '*_$#@!^%'                     #Creating huge string consisting of letters,numbers and special characters

    password = ''.join(random.choice(ch) for _ in range(l))                    #Randomly selecting characters from ch and appending to outputted rando pasword

    return password
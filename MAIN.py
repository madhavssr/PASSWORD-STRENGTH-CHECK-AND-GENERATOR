import PASSWORD_LENGTHCHECK
import PASSWORD_CHARACTERVAR
import STRENGTH_RESULT
import random
import string
import PASSWORD_GEN

print("PASSWORD STRENGTH CHECK AND GENERATOR")

print("\n1.Strength Check")
print("2.Random Password Generator")

x=input("\nMake your selection(1 or 2):")

if int(x)==1:
    print("STRENGTH CHECK")
    passw=input("\nEnter your password:")
    
    result1=PASSWORD_LENGTHCHECK.length_check(passw)
    if result1==True:
        print ("\n\nYour password is of sufficient length")
    else:
        print("\n\nYour password is not long enough")
    
    result2=PASSWORD_CHARACTERVAR.character_variation(passw)
    if result2==True:
        print("\n\nYour password has letter,numbers and symbols)
    else:
        print("\n\nYour password does not contain ayleast one letter,number or symbol each")
    
    STRENGTH_RESULT.strength_report(result1, result2)

if int(x)==2:
    print("RANDOM PASSWORD GENERATOR")
    
    
    x= PASSWORD_GEN.password_generator()
    print(x)
    
            
            
            
        
        

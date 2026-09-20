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
    print ("\n\nLength Check Passed:", result1)
    
    result2=PASSWORD_CHARACTERVAR.character_variation(passw)
    print("Character Variance Passed:", result2)
    
    STRENGTH_RESULT.strength_report(result1, result2)

if int(x)==2:
    print("RANDOM PASSWORD GENERATOR")
    
    
    x= PASSWORD_GEN.password_generator()
    print(x)
    
            
            
            
        
        

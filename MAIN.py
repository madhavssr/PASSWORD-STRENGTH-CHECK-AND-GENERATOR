import PASSWORD_LENGTHCHECK
import PASSWORD_CHARACTERVAR
import STRENGTH_RESULT
import PASSWORD_GEN



while True:      #To restart program after completion
    print("\n\n--------------------------------------------------------------------")
    print("\nPASSWORD STRENGTH CHECK AND GENERATOR")


    print("\n1.Strength Check")                                                #creating main menu
    print("2.Random Password Generator")
    print("3.Exit Program")
    x=input("\nMake your selection(1 ,2,or 3):")                               #Accepting user choice

    if int(x)==1:
        print("\nSTRENGTH CHECK")
        passw=passw = input("\nEnter your password:")
    
        result1=PASSWORD_LENGTHCHECK.length_check(passw)                       #Accessing length_check function from password_lengthcheck.py
        
    
        result2=PASSWORD_CHARACTERVAR.character_variation(passw)               #Accessing character_variation function from pass_chaactervar.py
        
    
        STRENGTH_RESULT.strength_report(result1, result2)                      #Printing strength report based on two tests
        print("\n\nRestarting Program...")
    
    
    elif int(x)==2:
        print("\n\nRANDOM PASSWORD GENERATOR")
    
    
        y= PASSWORD_GEN.password_generator()                                   #Accessing password_generator function from password_gen.py
        print(y)
        print("\n\nRestarting Program...")
    
    elif int(x)==3:
        print("\nTHANK YOU FOR USING THE PROGRAM.")
        break                                                                  #Exits loop,prevents program restart
    else:                                                                     
        print("Invalid Choice.")
        print("\n\nRestarting Program...")
        
    
    
            
            
            
        
        
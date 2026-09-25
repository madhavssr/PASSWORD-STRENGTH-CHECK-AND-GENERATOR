def character_variation(x):
    flag1=0                                                                    #Setting flag variables
    flag2=0
    flag3=0
    
    for i in x:
        if i.isupper():                                                        #Checking if password contains capital letter   
            flag1=1
        elif i.isdigit():                                                      #Checking if password contains a number
            flag2=1
        elif i.isalnum():
            continue
        else:                                                                  #Checking if password contains a special character
            flag3=1
    
    if flag1==1 and flag2==1 and flag3==1:                                     #Checking if flags were activated 
        return True
    else:
        return False
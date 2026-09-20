def character_variation(x):
    caps=0
    num=0
    spcl=0
    
    for i in x:
        if i.isupper():
            caps+=1
        elif i.isdigit():
            num+=1
        elif i.isalnum():
            continue
        else:
            spcl+=1
    
    if caps!=0 and num!=0 and spcl!=0:
        return True
    else:
        return False
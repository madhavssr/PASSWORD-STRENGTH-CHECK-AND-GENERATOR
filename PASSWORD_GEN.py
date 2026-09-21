import random
import string
def password_generator():
    l=int(input("Enter length of required password:"))
    ch=string.ascii_letters+string.digits+'*'+'_'+'$'+'#'+'@'+'!'+'^'+'%'
    
    password = ''.join(random.choice(ch) for _ in range(l))

    return password
    


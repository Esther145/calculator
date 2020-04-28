def add(x,y):
    z=x+y
    return z
def sub(x,y):
    z=x-y
    return z
def mul(x,y):
    z=x*y
    return z
def div(x,y):
    if(y==0):
        print("DIVISION BY ZERO!!!ERROR!!")
        return 'not defined'
    else:
        z=x/y
        return z 
def mod(x,y):
    if(y==0):
        print("DIVISION BY ZERO!!!ERROR!!")
        return 'not defined'
    else:
        z=x%y
        return z
    

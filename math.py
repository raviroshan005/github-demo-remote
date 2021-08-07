# add implementation
def add(x,y):
    return x+y
#subtract implementation
def subtract(x,y):
    return x-y    #on master
#multiply implementation
def multiply(x,y):
    return x*y    #on bug456
#divide implementation
def divide(x,y):
    if y==0:       #on master   
        return divide_by_0_error
    else:
        return x/y    

# square implementation
def square(x):
    return x*x
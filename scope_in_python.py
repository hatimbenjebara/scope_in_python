#scope 
x = 200 #global variable or global scope
def outside_function():
    y=100 #variable local or scope 
    print(x)
    print(y)
outside_function()
print(x)
#print(y) will give you error
def new_function():
    global y #incase you want to call global variable from inside function 
    y= 350
    print(x)
    print(y)
new_function()
print(x)
print(y)
def inside_functi():
    y=500
    def inside_function():
        x= 300 #local scope
        print(x)
    inside_function()
    print(y)
inside_functi()

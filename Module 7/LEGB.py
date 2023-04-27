x='is a global' #global
a=min([10,2,7,8,9]) #inbuilt
print(a)
def test():
    global x
    #local variable
    x='is a local'
    y='is a second local'
    print(y)
    print(x)
test()
print(x)
def unit_test(z):
    print(z)

unit_test('is a local variable')



#for enclosing variable

def outer():
    x='outer x'
    def inner():
        nonlocal x
        x='inner x'
        print(x)
    inner()
    print(x)
outer()
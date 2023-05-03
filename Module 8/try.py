def div(x,y):
    try:
        result= x //y
        print("your answer is : ",result)
    # except ZeroDivisionError:
    #     print("sorry ! can't divide by Zero")


    #another way of using except statement

    except Exception as e:
        print("this error is: ",e)
    
div(3,0)
div(3,"gg")


#using else clause
def Cat(a,b):
    try:
        c=((a+b)//(a-b))
    except ZeroDivisionError:
        print("a/b results in 0")
    else:
        print(c)
Cat(2.0,3.0)
Cat(3,3)


#finally keyword 

try:
    f=open('tes.txt')
except FileNotFoundError as e:
    print(e)
#general exception always at bottom    
except Exception as e:
    print('error')
else:
    print(f.read())
    f.close()
finally:
    print("executing finally....")

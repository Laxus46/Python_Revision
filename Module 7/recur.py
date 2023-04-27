#using these three steps we can convert any iterative func in recursive
#write  an iterative func to solve problem
#write a dispatcher function

def totaldiff(A,B,size):
    diff = 0
    for i in range(size):
        diff+=abs(A[i]-B[i])
    return diff


def totalDispatcher(A,B,size):
    if(size==0):
        return 0
    lastEl=abs(A[size-1]-B[size-1])
    diff=totalDispatcher(A,B,size-1)+lastEl
    return diff


A=[15,-4,56,10,-23]
B=[14,-9,56,14,-23]

x= totaldiff(A,B,5)
y=totalDispatcher(A,B,5)

print(x,y)
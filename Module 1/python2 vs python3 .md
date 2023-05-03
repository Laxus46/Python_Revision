# Module 1

- **Important differences between Python 2.x and Python 3.x:
Division operator**
    
    ```python
    print 7 / 5
    
    print -7 / 5	
    
    '''
    
    Output in Python 2.x
    
    1
    
    -2
    
    Output in Python 3.x :
    
    1.4
    
    -1.4
    ```
    
- **print function:**
    
    ```python
    print'hello world' #doesn't work in python 3.x
    print("hello world") #works in python3.x not in python2.x
    ```
    

- **Unicode**
    
    In Python 2, an implicit str type is ASCII. But in Python 3.x implicit str type is
    
- **xrange**
    
    ```python
    for x in xrange(1, 5):
    
    	print(x),
    
    for x in range(1, 5):
    
    	print(x),
    
    '''
    
    Output in Python 2.x
    
    1 2 3 4 1 2 3 4
    
    Output in Python 3.x
    
    NameError: name 'xrange' is not defined
    
    '''
    ```
    
- **Error Handling**
    
    ```python
    There is a small change in error handling in both versions.
     In python 3.x, ‘as’ keyword is required.
    ```
    
- **__future __module**
    
    This is basically not a difference between the two versions, but a useful thing to mention here. The idea of the __future__ module is to help migrate to Python 3.x.
    
    If we are planning to have Python 3.x support in our 2.x code, we can use
    
    **_future_**imports in our code.
# Module 1

- **Important differences between Python 2.x and Python 3.x:**
    - **Division operator**
        
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
        
- **Python vs other language**
    
    Differences between Python and Other Programming Languages
    
    - Python is an interpreted and dynamically typed language, whereas Java and C++ are compiled and statically typed languages.
    - Python has a simpler syntax than many other programming languages, making it easier to learn and use.
    - Python is often used for scripting, automation, and data analysis, whereas Java is often used for developing large-scale enterprise applications and C++ is often used for system programming and high-performance computing.
    - Python is often used for server-side scripting, whereas JavaScript is often used for client-side scripting.
    - Python supports modules and packages, which encourages program modularity and code reuse.
    - Python has built-in data structures and dynamic typing, which make it attractive for rapid application development and scripting.
    - Python does not require compilation before running, which makes the edit-test-debug cycle faster.
    - Python has a large and extensive standard library that is available in source or binary form without charge for all major platforms.
- **Python run**
    
    Python is an interpreted language, which means that it does not need to be compiled before it can be executed. Instead, the Python interpreter reads the source code and executes it line by line. Here's a brief overview of how Python runs:
    
    1. The Python interpreter reads the source code or instruction and verifies that there are no syntax errors.
    2. If there are no syntax errors, the interpreter converts the source code into bytecode, which is a lower-level representation of the code that can be executed by the Python virtual machine (PVM) .
    3. The PVM then executes the bytecode, which involves interpreting each instruction and carrying out its operation.
    4. As the bytecode is executed, the PVM keeps track of the state of the program, including the values of variables and the call stack.
    5. When the program finishes executing, the PVM exits and any resources used by the program are released.# Module 1

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
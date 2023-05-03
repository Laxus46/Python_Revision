
- **Modules in python**
    
    When the interpreter executes the above `import` statement, it searches for `mod.py` in a [list](https://realpython.com/python-lists-tuples/) of directories assembled from the following sources:
    
    - The directory from which the input script was run or the **current directory** if the interpreter is being run interactively
    - The list of directories contained in the `[PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)` environment variable, if it is set. (The format for `PYTHONPATH` is OS-dependent but should mimic the `[PATH](https://realpython.com/add-python-to-path/)` environment variable.)
    - An installation-dependent list of directories configured at the time Python is installed
    
    ## **The import Statement**
    
    **Module** contents are made available to the caller with the `import` statement. The `import` statement takes many different forms, shown below.
    
    ```python
    ****import <module_name>****
    
    ```
    
    Several comma-separated modules may be specified in a single `import` statement:
    

```python
import <module_name>[, <module_name> ...]
```

### **`from <module_name> import <name(s)>`**

An alternate form of the `import` statement allows individual objects from the module to be imported *directly into the caller’s symbol table*:

```python
from <module_name> import <name(s)>
>>> from module import add
>>> add(3,4)
sum = 7
>>> from module import *
>>> greeting('laxus')
Hello, laxus
>>> add(6,7)
sum = 13
>>>
```

### **`import <module_name> as <alt_name>`**

You can also import an entire module under an alternate name:

```python
from module import add as a
>>> a(3,4)
sum = 7
```

Lastly a try statement with an except ImportError  clause can be used to guard against unsuccessful `import` attempts:>>>

```python
>>> try: 
...  from module import hero
... except ImportError:
...  print("object not found")
```

- **Packages in python**
    
    Python packages are a way of structuring Python's module namespace by using "dotted module names". A package is a collection of modules that are organized in a directory hierarchy. A package can contain sub-packages, which in turn can contain sub-packages themselves, forming a tree-like structure. The Python Package Index (PyPI) is a repository of software for the Python programming language. PyPI helps you find and install software developed and shared by the Python community. PyPI is the default package manager for Python, and it can be used to install packages using the command.
    
    ```
    pip
    ```
    
    To create a Python package, you need to create a directory with a special file called
    
    ```
    __init__.py
    ```
    
     This file can be empty or can contain initialization code for the package. You can then create modules inside the package directory, which can be imported using dotted module names
    
    ```python
    mypackage/
        __init__.py
        module1.py
        module2.py
    ```
    
    .
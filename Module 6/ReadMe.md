# module 6

- **if and else:**
    
    ```python
    >>> x=0
    >>> y=5
    >>> if x<y:
    ...  print('yes')
    ... 
    yes
    >>> if y<x:
    ...  print('yes')
    ... 
    >>> if x:
    ...  print('yes')
    ... 
    >>> if x or y :
    ...  print('yes')
    ...
    yes
    >>> if 'aul' in 'grault':
    ...  print('yes')
    ...
    yes
    ```
    
    ****The else and elif Clauses:****
    
    ```python
    if <expr>:
        <statement(s)>
    else:
        <statement(s)>
    ```
    
    ```python
    if <expr>:
        <statement(s)>
    elif <expr>:
        <statement(s)>
    elif <expr>:
        <statement(s)>
        ...
    else:
        <statement(s)>
    ```
    
    ****One-Line if Statements:****
    
    ```python
    if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
    ```
    
    But what does this mean? There are two possible interpretations:
    
    1. If `<expr>` is true, execute `<statement_1>`.
        
        Then, execute `<statement_2> ... <statement_n>` unconditionally, irrespective of whether `<expr>` is true or not.
        
    2. If `<expr>` is true, execute all of `<statement_1> ... <statement_n>`. Otherwise, don’t execute any of them.
- **Notes**
    - **If-else and Elif Statements:**
        - The **`if`** statement is used to test a condition, and the code inside the block is executed only if the condition is true.
        - The **`else`** statement is optional and provides a block of code to execute when the condition in the **`if`** statement is false.
        - The **`elif`** statement allows you to test multiple conditions and execute a different block of code for each condition.
    - **Pass and Range Keywords**:
        - The **`pass`** keyword is a placeholder statement that does nothing. It's often used as a placeholder when you're working on code that you haven't implemented yet.
        - The **`range()`** function generates a sequence of numbers. It takes up to three arguments: **`start`**, **`stop`**, and **`step`**. The **`start`** and **`step`** arguments are optional.
    - **While and For Loops and Else**:
        - The **`while`** loop is used to repeat a block of code as long as a certain condition is true.
        - The **`for`** loop is used to iterate over a sequence (such as a list, tuple, or string).
        - The **`else`** block is optional and is executed when the loop is finished.
    - **Nesting Loops and Conditionals:**
        - You can nest loops and conditionals inside each other to create more complex logic.
        - When nesting loops, each inner loop will execute completely for each iteration of the outer loop.
    - **Break and Continue Statements:**
        - The **`break`** statement is used to exit a loop early.
        - The **`continue`** statement is used to skip an iteration of a loop and move on to the next iteration.
    - **List Comprehension:**
        - List comprehension is a concise way to create a new list from an existing sequence or iterable.
        - The syntax is **`[expression for item in iterable]`**.
        - The expression is applied to each item in the iterable to create a new item in the list.
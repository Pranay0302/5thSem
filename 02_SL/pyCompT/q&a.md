1. What are the datatypes in python? Describe all of them with code examples.

 - datatypes are classification of the data items.

    > string  (sequence type)

    ```
    str = 'hello bye'
    ```
    > number (numeric type)
    ```
    a = 9 
    print(type(a))

    b = 9.0
    print(type(b))

     ```
    > dictionary  (dicts are used to store the data in key:value pairs)
        - ordered
        - changeable (mutable)
        - doesn't allow duplicates

    ```
        stockData = {
            "Company" : "TSLA",
            "Price" : 1023
        }
    ```

    > tuples (tuples are collection of python objects, can include **mixed datatypes** and **nested datatypes** in a list)
        - ordered
        - unchangeable (immutable)
        - allow duplicates
    ```
    tup = (('keshi', 2, 'charli'), (0,1,2,3))
    ```

    > lists (lists are also collection of python objects which include hetereogeneous elements)
        - ordered
        - changeable (mutable)
        - allow duplicates

    ```
        meds = ["ciplox", "dolo", "auffceff", "cobuilt"]
    ```

2. What is the difference between a list and an array in python ?
    > lists can store heterogeneous elements and arrays can store only homogeneous elements
3. Why is a tuple called immutable ?
    > tuples are immutable since they're sequence of heterogeneous elements which can be accessed through indexing and it doesn't support item assignment
4. How do you define a function in python. Give code examples. What is the significance of
indentation ?
    > functions are reusable block of code. 3
    ```
    def check():
        print("checking")
    check()
    ```
    > indentation is imp. since the py intepreter will execute the block of code and give proper results.
5. Illustrate with code example use of import.
    ```
    import datetime as dt

        print(dt.date.today())
    ```
6. How to write a for loop in python using an iterator.
    ```
        x = ['btc', 'eth', 'bnb']
        for i in x:
            print(i)
    # x is the <iterable> and i is the <variable>

    ```
7. What do you mean by slicing in python?
    > slicing is a method which returns a slice object
    > slice(start:end:step)
8. What do you mean by splicing in python?
    > splicing is a method from which we can access any character or sub string from a string
9. What is the difference between slicing and splicing in python?
    > slice cannot change the array and whereas using splice will change
10. Why is python called a scripting language?
> * typecasting (implicit & explicit)
> * intepreter is used to translate code and execute at runtime
> * can do automated stuff

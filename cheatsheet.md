# Basic Concepts

## 1. Variables

- spaces, special characters are not allowed.
  
- Variables can  start with alphabets and underscore.

    **Valid Variables** :    x=10,name="tharun", country_name="India"

    **Invalid Variables** :  56name="arun", user@name="sachin", my number = 991234



## 2. Data Types

- Primitive data types : int, float , bool , complex ,str
- Non-primitive data types : list, tuple , set , dict

## 3. Type Checking

    type("x") : <class 'str'>  <!-- prints the data type of x  as string-->

    type(100) : <class 'int'>  <!-- Prints the data type of 100 as integer-->

    type(True) : <class 'bool'> <!-- Prints the data type of True as bool-->

## 4.Type Conversion

    int("100") : 100 . Here 100 converted from string to integer.

    float(5) = 5.0 

## 5. Operators 

- Arithmetic operators : + , - , * , / , // , % , **.

- Comparison OPerators : == , ! = , > , < , >= , <=.

- Logical operators : and, or , not.

- Bitwise Operators  

- Bitwise operators works on binary digits of numbers.
  
- & (AND) -> Both bits must be 1  ex:- 5 & 3 = 1

- | (OR) -> If at least one bit is 1 .  ex:-  5 | 3 = 7

- ^ (XOR) -> If bits are different ,result is 1.  ex:- 5^3 = 6.

- ~ (NOT/Complement) -> Flip bits i.e (0->1, 1->0)  ex:- ~5  = -6 because python uses 2's complement representation.


## 6. Conditional operators 

- if, else, elif are  conditional keywords.
  
   ```bash
      age=18
      if(age<18):
        print("child")
      elif(18<=age<=60):
        print("Middle aged")
      else:
        print("elder aged")
    ```

## 7. Loops

### For loop

 - For loop is used when number of iterations is known.
   ```bash 
     for i in range(10):
        print(i)
   ```

### While loop
 - While is a condition based loop.

    ```bash
        x=1
        while x<15:
            print("tharun")
            x=x+1
    ```

## 8 .Functions
- Functions are used to reuse code, defined using def keyword.

- **Using default parameters.**

  ```bash
  def greet(name="Virat"):
    print(name)
  ```

- *args and **kwargs

   ```bash
    def fun(*args):
        print(args)

    def fun(**kwargs):
        print(kwargs)
   ```

## 9. Object Oriented Programming (Basic)

- class creation

  ```bash
     class person:
        def __init__(self,name):
            self.name=name

        def greet(self):
            print("hello",self.name)
  ```
- Objects creation

   ```bash
        p = Person("Tharun")
        p.greet()
   ```

# Popular String methods

- Strings are immutable(they cannot be changed).


### 1. Case Conversion

- **upper()**    Converts all letters to uppercase

  ```bash
   "hello".upper()  # HELLO
    ```
- **lower()**  Converts all letters to lowercase

  ```bash
   "HELLO".lower() # hello
  ```
-  **title()**  Capitalizes the first letter of each word

   ```bash
     "hello world".title()  # "Hello World" 
   ```
- **capitalize()**  Capitalizes the first letter of the string

  ```bash
    "hello world".capitalize()  # "Hello world"
  ```

### 2. Removing spaces

- **strip()**  Removes spaces from both ends

   ```bash
     " hi ".strip() # "hi"
   ```

  ```bash
      "$$hello&$".strip("$&")  # "hello"
  ```

### 3. searching / Counting

- **find(substring)** Returns the index of substring (-1 if not found)
  
  ```bash
  "hello".find("o") # 4 
  ```
- **index(substring)**  Returns the index (error if not found).

    ```bash
    "hello".index("e") # 1
    ```
  
-  **count(substring)** Counts occurences of substring.
    ```bash
    "hello".count("l") # 2
    ```
### 4. Validation Methods

  - **isdigit()** check if string has only digits.
  
     ```bash
       "123".isdigit()  # True
     ```
-  **isalpha()** check if string has only letters.
    ```bash
        "abc".isalpha()  # True
    ```
- **isspace()** check if string has only spaces.
    ```bash
       "   ".isspace() # True
    ```
### 5. Modification Strings

- **replace(old,new)**  Replaces substring

  ```bash
  "hello".replace("l", "t")  # "hetto"
  ```
- **split(separator)** Split strings into list

  ```bash
  "a-b-c".split("-") # ['a','b','c']
  ```
- **join(iterable) joins list into string
  ```bash
  ",".join(['a','b','c']) # "a,b,c"

#  Popular list methods

### 1. Elements Addition


- append(x)  adds element x at end
```bash
lst=[3,4]
lst.append(1)  #[3,4,1]
```
- insert(index,x) add element x at index position.
  ```bash
  lst.insert(1,56) # [3,56,4,1]
  ```
### 2. Removing Elements

-  **pop()**  Removes and returns last element
  
   ```bash
        lst.pop()  # 7   lst = [3,56,4]
   ```
- **remove(x)**  removes first occurence of x 
  ```bash
  lst.remove(4)  # lst = [3,56] 
  ```
- **lst.clear()**  clears all elements.
  ```bash
  lst.clear() # []
  ```

###  3. Sorting Elements

- **sort()** sorts list in ascending order.
  
  ```bash
  [5,3,7].sort() # [3,5,7]
  ```
- **sort(reverse=True)**  sort list in descending order.
  ```bash
  [5,3,7].sort(reverse=True) # [7,5,3] 
  ```

# Popular Dictionary Methods

    d= {"a":1,"b":2,"c":5}

### 1. Accessing values

 - d.get(a,default_Value)  Returns default if key found.
  
    ```bash
     d.get("y",5) # 5 because there is no key named y.  
    ```
### 2. Adding/Updating values

  - **d.update({"e":6,"f":8})**  Add multiple items
  
  ```bash
  d.update({"e":6,"f":9}) # d={"a":1,"b":2,"c":5,"e":6,"f":8}
  ```
### 3. Removing items
  
  - **d.popitem()**  removes last key-value pair

    ```bash
    d.popitem() # d={"a":1,"b":2,"c":5,"e":6}
    ```
 - **d.clear()** Removes all elements.
   ```bash
   d.clear() # d={}
   ```

### 4. Dictionary comprehension

  - Build dictionary using loops and conditions in one line.
 
  ```bash
   square_dict = {x: x*x for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
  ```

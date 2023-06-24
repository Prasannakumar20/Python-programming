


#1.write a python program get an integer input from a user. If the number is odd, then find the factorial of a number and find the number of digits in the factorial of the number. If the number is even, then check the given number is palindrome or not.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(n):
    # Convert the number to a string and check if it's equal to its reverse
    return str(n) == str(n)[::-1]

# Get input from the user
number = int(input("Enter an integer: "))

if number % 2 != 0:  # Odd number
    # Calculate the factorial of the number
    fact = factorial(number)

    # Calculate the number of digits in the factorial
    num_digits = len(str(fact))

    print("Factorial of", number, "is:", fact)
    print("Number of digits in the factorial:", num_digits)

else:  # Even number
    if is_palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")

#2.write a python program to check whether the second string can be obtained from the first by deletion of none, one or more characters.

        
def is_obtainable(first_str, second_str):
    if len(second_str) > len(first_str):
        return "NO"

    for char in second_str:
        if char not in first_str:
            return "NO"

    return "YES"

# Example usage
first_str = "abcdef"
second_str = "bcf"
result = is_obtainable(first_str, second_str)
print(result)  # Output: YES

second_str = "xyz"
result = is_obtainable(first_str, second_str)
print(result)  # Output: NO




#3.A)write a Python Program for positive and negative indexing in Lists

#Positive indexing example
my_list = ['a', 'b', 'c', 'd', 'e']

#Accessing elements using positive indexing
print(my_list[0])    
print(my_list[2])    
print(my_list[4])    
#Negative indexing example
my_string = "Hello, World!"

#Accessing elements using negative indexing
print(my_string[-1])    
print(my_string[-6])    
print(my_string[-13])





#3.B)write a Python Program to check whether the list given is in ascending order or not

def is_ascending_order(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Example usage
list1 = [1, 2, 3, 4, 5]
print(is_ascending_order(list1))   

list2 = [5, 3, 1, 4, 2]
print(is_ascending_order(list2))




#4.A)write a Python Program to convert the tuple to a string.


def str1(t):
    res = ' '
    for item in t:
        res = res + item
    return res

n=int(input("Enter number of elements in tuple "))
l=list()
for i in range(0,n):
    e=input("enter the value")
    l.append(e)
a=tuple(l)
print(“The string is “, str1(a))


#4.B)write a Python Program to reverse a tuple.


def reverse_tuple(tuple_value):
    reversed_tuple = tuple_value[::-1]
    return reversed_tuple

# Example usage
my_tuple = (1, 2, 3, 4, 5)
result = reverse_tuple(my_tuple)
print(result)  
another_tuple = ('a', 'b', 'c', 'd', 'e')
result = reverse_tuple(another_tuple)
print(result)



#5.write a python program to check if a set is a subset of another set.


def is_subset(set1, set2):
    return set1.issubset(set2)

# Example usage
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(is_subset(set1, set2))  

set3 = {4, 5, 6}
set4 = {1, 2, 3}
print(is_subset(set3, set4))



#6.write a python program to iterate over dictionaries using for loop


# Iterating over keys
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Iterate over keys
print("Iterating over keys:")
for key in my_dict:
    print(key)
print("\n")

# Iterating over values
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Iterate over values
print("Iterating over values:")
for value in my_dict.values():
    print(value)

print("\n")

# Iterating over key-value pairs
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Iterate over key-value pairs
print("Iterating over key-value pairs:")
for key, value in my_dict.items():
    print(key, "->", value)

#7.A) write a python program to convert a list of numeric value into a one-dimensional Numpy array.


    import numpy as np

# List of numeric values
my_list = [1, 2, 3, 4, 5]

# Convert list to NumPy array
my_array = np.array(my_list)

# Print the NumPy array
print(my_array)



#7.B)write a Python program to convert a list and tuple into arrays using Numpy.


import numpy as np

# Convert a list to a NumPy array
my_list = [1, 2, 3, 4, 5]
list_array = np.array(my_list)

# Convert a tuple to a NumPy array
my_tuple = (6, 7, 8, 9, 10)
tuple_array = np.array(my_tuple)

# Print the NumPy arrays
print("List array:", list_array)
print("Tuple array:", tuple_array)



#8.A)write a python program to convert a NumPy array and series to dataframe.

arr = np.random.rand(3) #to create an one dimensional array 
print("Numpy array:")
print(arr)
#conversion of array to dataframe
d = pd.DataFrame(series,columns =['A'])
print("\nArray to DataFrame: ")
#conversion of array to series
series = pd.Series(arr)
print("Series : ")
display(series)
# conversion of series to dataframe
df = pd.DataFrame(series,columns =['A'])
print("\nSeries to DataFrame: ")
df

#8.B)write a python program to add, subtract, multiply and divide two pandas series.


ds1 = pd.Series([12, 45, 6, 81, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Addition of two Series:")
print(ds)
print("Subtraction of two Series:")
ds = ds1 - ds2
print(ds)import pandas as pd

print("Multiplication of two Series:")
ds = ds1 * ds2
print(ds)
print("Division of Series1 by Series2:")
ds = ds1 / ds2
print(ds)





#8.C)Program to retrieve and manipulate data using dataframes.


import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'Eva'],
    'Age': [25, 32, 28, 41, 36],
    'Country': ['USA', 'Canada', 'UK', 'USA', 'Australia'],
    'Salary': [5000, 7000, 6000, 8000, 6500]
}

df = pd.DataFrame(data)

# Retrieve data from the DataFrame

# Access a single column
name_column = df['Name']
print("Name column:")
print(name_column)

# Access multiple columns
age_salary_columns = df[['Age', 'Salary']]
print("\nAge and Salary columns:")
print(age_salary_columns)

# Access a single row by index
row_2 = df.loc[2]
print("\nRow at index 2:")
print(row_2)

# Access a subset of rows using conditions
usa_rows = df[df['Country'] == 'USA']
print("\nRows with Country as USA:")
print(usa_rows)

# Manipulate data in the DataFrame

# Add a new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus column:")
print(df)

# Update values in a column
df.loc[3, 'Age'] = 42
print("\nDataFrame with updated Age value:")
print(df)

# Delete a column
df.drop('Salary', axis=1, inplace=True)
print("\nDataFrame with Salary column deleted:")
print(df)























        

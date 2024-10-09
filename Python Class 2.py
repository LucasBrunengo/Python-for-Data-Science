'''
#Exercise 1: FizzBuzz

1. Write a FizzBuzz Function: Create a function fizzbuzz(n) that takes an integer n as a parameter.

2. Implement FizzBuzz Logic: The function should print:
     * "Fizz" for multiples of 3
     * "Buzz" for multiples of 5
     * "FizzBuzz" for multiples of both 3 and 5
     * The number itself for other numbers

3. Call the Function: Call the function for numbers 1 to 20.
'''

def fizzbuzz(n) : 
    for i in range(1, n + 1) :
        if i % 3 == 0 and i % 5 == 0 : 
            print("FizzBuzz") 
        elif i % 3 == 0 : 
            print("Fizz")
        elif i % 5 == 0 : 
            print("Buzz")
        else :
            print(i)

fizzbuzz(20)

'''
Exercise 2: Basic Data Filtering

1. Create a List of Mixed Data Types: Create a list that contains a mix of integers, strings, and floats.

2. Filter the List: Use list comprehension to create a new list that contains only the integers from the original list.

3. Print the New List: Output the filtered list of integers.
'''

Mixed_List = ["Lucas", 24, 24.7, "Agustin", 27, 27.9, "Manuel", 18, 18.1]

Int_List = [x for x in Mixed_List if isinstance(x, int)]

print(Int_List)


'''
Exercise 3: Simple To-Do List

1. Create an Empty List: Start with an empty list called todo_list.

2. Define Functions:
    * A function add_task(task) that adds a task to the list.
    * A function show_tasks() that prints all tasks in the list.
'''

todo_list = []

def add_task(task) :
    todo_list.append(task)
    print(f"'{task}' added to do the list")

def show_tasks() : 
    if not todo_list :
        print("The list is empty")
    else : 
        print(todo_list)


add_task("Buy milk")
add_task("Call dad")
show_tasks()

'''
Exercise 4: Temperature Converter

1. Define a Conversion Function: Write a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit.

2. Print the Result: Output the converted temperature for 22ºF, 46ºF, 51ºF and 76ºF.
'''

def celsius_to_fahrenheit(celsius) :
    return (celsius * 1.8) + 32

print(f"22ºC equals to {celsius_to_fahrenheit(22)}ºF")
print(f"46ºC equals to {celsius_to_fahrenheit(46)}ºF")
print(f"51ºC equals to {celsius_to_fahrenheit(51)}ºF")
print(f"76ºC equals to {celsius_to_fahrenheit(76)}ºF")

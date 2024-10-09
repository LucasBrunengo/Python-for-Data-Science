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

def fizzbuzz(n): 
    # Loop through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if the number is a multiple of both 3 and 5
        if i % 3 == 0 and i % 5 == 0: 
            print(f"{i}: FizzBuzz")  # Output for multiples of both 3 and 5
        elif i % 3 == 0:
            print(f"{i}: Fizz")  # Output for multiples of 3
        elif i % 5 == 0:
            print(f"{i}: Buzz")  # Output for multiples of 5
        else:
            print(f"{i}: {i}")  # Output the number itself if it’s not a multiple of 3 or 5


# Call FizzBuzz function for numbers 1 to 20
fizzbuzz(20)

# (See screenshot of execution: 
#   - Input: (Screenshots/Session%202/Inputs/Session2_Ex1_Inp_FizzBuzz.png)
#   - Output: (Screenshots/Session%202/Outputs/Session2_Ex1_Out_FizzBuzz.png))

'''
Exercise 2: Basic Data Filtering

1. Create a List of Mixed Data Types: Create a list that contains a mix of integers, strings, and floats.

2. Filter the List: Use list comprehension to create a new list that contains only the integers from the original list.

3. Print the New List: Output the filtered list of integers.
'''

# Create a list with mixed data types: strings, integers, and floats
Mixed_List = ["Lucas", 24, 24.7, "Agustin", 27, 27.9, "Manuel", 18, 18.1]

# Create a new list that filters only integers from Mixed_List
Int_List = [x for x in Mixed_List if isinstance(x, int)]

print("Filtered list of integers:", Int_List)  # Output the filtered list of integers

# (See screenshot of execution: 
#   - Input: (Screenshots/Session%202/Inputs/Session2_Ex2_Inp_DataFiltering.png)
#   - Output: (Screenshots/Session%202/Outputs/Session2_Ex2_Out_DataFiltering.png))

'''
Exercise 3: Simple To-Do List

1. Create an Empty List: Start with an empty list called todo_list.

2. Define Functions:
    * A function add_task(task) that adds a task to the list.
    * A function show_tasks() that prints all tasks in the list.
'''

# Initialize an empty list to hold tasks
todo_list = []

# Function to add a task to the todo_list
def add_task(task):
    todo_list.append(task)  # Add the task to the end of the list
    print(f"'{task}' has been added to the to-do list")  # Inform the user that the task was added

# Function to display all tasks in the todo_list
def show_tasks(): 
    # Check if the todo_list is empty
    if not todo_list:
        print("The list is empty")  # Inform the user that there are no tasks
    else: 
        print("Current tasks in the to-do list:", todo_list) # Output all tasks in the list

# Add tasks to the to-do list
add_task("Buy milk")  # Adding a task: "Buy milk"
add_task("Call dad")  # Adding another task: "Call dad"
show_tasks()  # Display all tasks in the list

# (See screenshot of execution: 
#   - Input: (Screenshots/Session 2/Inputs/Session2_Ex3_Inp_ToDoList..png)
#   - Output: (Screenshots/Session 2/Outputs/Session2_Ex3_Out_ToDoList.png))

'''
Exercise 4: Temperature Converter

1. Define a Conversion Function: Write a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit.

2. Print the Result: Output the converted temperature for 22ºF, 46ºF, 51ºF and 76ºF.
'''

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Conversion formula: (Celsius * 1.8) + 32
    return (celsius * 1.8) + 32

# Print the converted temperatures using the conversion function
print(f"22ºC equals to {celsius_to_fahrenheit(22)}ºF")
print(f"46ºC equals to {celsius_to_fahrenheit(46)}ºF")
print(f"51ºC equals to {celsius_to_fahrenheit(51)}ºF")
print(f"76ºC equals to {celsius_to_fahrenheit(76)}ºF")

# (See screenshot of execution: Screenshots/Session 2. Ex 4. Temperature converter.png)


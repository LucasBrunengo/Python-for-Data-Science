# Exercise 1: Print a Greeting

greeting = "Hello, Python"  # Assign a greeting message to the variable

print(greeting)  # Output the greeting message


# Exercise 2: Basic Arithmetic

a = 10  # First number
b = 2   # Second number

# Performing basic arithmetic operations
summarize = a + b  # Sum of a and b
diff = a - b       # Difference between a and b
product = a * b    # Product of a and b
quotient = a / b   # Quotient of a divided by b

# Output results of arithmetic operations
print(f"The sum of {a} and {b} is: {summarize}")  # Print sum
print(f"The difference of {a} and {b} is: {diff}")  # Print difference
print(f"The product of {a} and {b} is: {product}")  # Print product
print(f"The quotient of {a} divided by {b} is: {quotient}")  # Print quotient

# Exercise 3: String Manipulation

name = "Lucas"  # Assign name to a variable

print(f"Hello, {name}!")  # Output a greeting including the name


# Exercise 4: Lists

universities = ["UCC", "ESADE", "UBA", "UNC", "UTN"]  # List of university names

print("List of universities:", universities)  # Output the list of universities
print(f"The first university is {universities[0]} and the last university is {universities[-1]}.")  # Output first and last university



# Exercise 5: Dictionaries

student = {
            "Lucas" : {
                "age" : 24, 
                "grade" : 10 
                }, # Student details for Lucas
            "Manuel" : {
                "age" : 17,
                "grade" : 9
                }, # Student details for Manuel
            }

print("Student information:", student)  # Output student information


# Exercise 6: Tuples

coordinates = (5, 10)  # Tuple representing coordinates (X, Y)

print(f"The X coordinate is: {coordinates[0]}")  # Output the X coordinate
print(f"The Y coordinate is: {coordinates[1]}")  # Output the Y coordinate


# Exercise 7: Sets

colors = {"red", "green", "blue"}  # Initial set of colors
colors.add("black")  # Add 'black' to the set
print("Current colors set after adding black:", colors)  # Output colors set

colors.add("black")  # Adding 'black' again (no change in set)
print("Colors set after trying to add black again (should remain unchanged):", colors)  # Output should remain unchanged

colors.remove("black")  # Remove 'black' from the set
print("Current colors set after removing black:", colors)  # Output the modified colors set

light_colors = {"light_red", "light_green", "light_blue"}  # Set of light colors
print("Light colors set:", light_colors)  # Output light colors set

# Merging colors sets
merged_colors = colors.union(light_colors)  # Union of the two sets
print("Merged colors set:", merged_colors)  # Output merged set of colors


# Exercise 8: Conditional Statements

EX8 = int(input("Enter a number: "))  # Get user input and convert to integer

# Check the value of the input number and output corresponding message
if EX8 > 0:
    print(f"The number {EX8} is positive!")  # Output if the number is positive
elif EX8 < 0:
    print(f"The number {EX8} is negative!")  # Output if the number is negative
else:
    print("The number is 0!")  # Output if the number is zero


# Exercise 9: For Loop

List_1 = [1, 2, 3, 4, 5]  # List of numbers

print("Printing all numbers in the list:")
# Loop through each number in the list and print it
for number in List_1:
    print(number)  # Output each number
else:
    print("All numbers have been printed!")  # Final message indicating completion


# Exercise 10: While Loop

counter = 1  # Initialize counter

print("Counting from 1 to 5:")

# While loop to count from 1 to 5
while counter <= 5:
    print(counter)  # Output current counter value
    counter += 1  # Increment counter
else:
    print("Loop Finished!")  # Final message indicating completion


# Exercise 11: Match Statement (Python 3.10+)

grade = input("Enter a grade: ").upper()  # Get user input for grade and convert to uppercase

if grade == "A" :
    print("Excellent") # Output for grade A
elif grade == "B" :
    print("Good Job") # Output for grade B
elif grade == "C" :
    print("Fair") # Output for grade C
elif grade == "D" :
    print("Needs Improvement") # Output for grade D
elif grade == "F" :
    print("Failing") # Output for grade F
else :
    print("Invalid Input. Enter a valid grade (A, B, C, D, F)") # Output for invalid grade


#Excercise 12: Define a Function

def greet(name) : 
    print(f"Hello, {name}")

greet("Lucas") # Function to greet a user


# Exercise 13: Function with Return Value

def square(number):
    return number ** 2  # Function to calculate square of a number

# Output squares of numbers 2 to 5
print(f"The square of 2 is: {square(2)}")  # Output for 2
print(f"The square of 3 is: {square(3)}")  # Output for 3
print(f"The square of 4 is: {square(4)}")  # Output for 4
print(f"The square of 5 is: {square(5)}")  # Output for 5

#Excercise 14: Function with Default Parameters

def multiply(a, b = 3) :
    return a * b # Function to multiply two numbers, with a default value for b

# Output multiplication of 3 by the default parameter 3
print(f"Multiplying 3 by default parameter 3 gives: {multiply(3)}")  # Output for 3


#Excercise 15

List_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Square_List_2 = [number ** 2 for number in List_2]

print(List_2)
print(Square_List_2)


#Excercise 16

students = {
    "Lucas" : [ 10, 8, 6, 10],
    "Manuel" : [10, 8, 10, 9],
    "Agustin" : [9, 7, 8, 8],
    "Carlos" : []
}

def avg_grades(student_grades):
    for student, grades in student_grades.items():
        if grades : 
            average = sum(grades) / len(grades)
            print(f"{student}: {average}")
        else:
            print(f"{student}: No record of grades.")

avg_grades(students)


#Excercise 17

def calculate(num_1, num_2, operator) :
    if operator == "+" :
        return num_1 + num_2
    elif operator == "-" : 
        return num_1 - num_2
    elif operator == "*" :
        return num_1 * num_2
    elif operator == "/" :
        if num_2 != 0 :
            return num_1 / num_2 
        else :
            return "Error. Divided by zero."
    else : 
        return "Invalid operator!"
    
num_1_input = float(input("Enter the first number : "))
num_2_input = float(input("Enter the second number: "))
operator_input = input("Enter de operator (+, -, *, /): ")

result = calculate(num_1_input, num_2_input, operator_input)
print(f"Result: {result}")


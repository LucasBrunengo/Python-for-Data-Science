# Python Exercises Repository

Welcome to my Python Exercises repository. 
This repository contains solutions to various exercises focused on Python programming concepts.

## Table of contents

---

- **[Session 1](#session-1)** 

   - [Exercise 1: Print a Greeting](#exercise-1-print-a-greeting)
   - [Exercise 2: Basic Arithmetic](#exercise-2-basic-arithmetic)
   - [Exercise 3: String Manipulation](#exercise-3-string-manipulation)
   - [Exercise 4: Lists](#exercise-4-lists)
   - [Exercise 5: Dictionaries](#exercise-5-dictionaries)
   - [Exercise 6: Tuples](#exercise-6-tuples)
   - [Exercise 7: Sets](#exercise-7-sets)
   - [Exercise 8: Conditional Statements](#exercise-8-conditional-statements)
   - [Exercise 9: For Loop](#exercise-9-for-loop)
   - [Exercise 10: While Loop](#exercise-10-while-loop)
   - [Exercise 11: Match Statement](#exercise-11-Match-Statement (Python 3.10+))
   - [Exercise 12: Define a Function](#exercise-12-define-a-function)
   - [Exercise 13: Function with Return Value](#exercise-13-function-with-return-value)
   - [Exercise 14: Function with Default Parameters](#exercise-14-function-with-default-parameters)
   - [Exercise 15: List Comprehension](#exercise-15-list-comprehension)
   - [Exercise 16: Nested Data Structures](#exercise-16-nested-data-structures)
   - [Exercise 17: Simple Calculator](#exercise-17-simple-calculator)

---

### 
- **[Session 2](#session-2)**

   - [Exercise 1: FizzBuzz](#exercise-1-fizzbuzz)
   - [Exercise 2: Basic Data Filtering](#exercise-2-basic-data-filtering)
   - [Exercise 3: Simple To-Do List](#exercise-3-simple-to-do-list)
   - [Exercise 4: Temperature Converter](#exercise-4-temperature-converter)

---

- **[Session 3](#session-3)**
   - **[Exercise 1: Course Class](#exercise-1-course-class)**
   - **[Exercise 2: Student Class](#exercise-2-student-class)**
   - **[Exercise 3: Registration Class](#exercise-3-registration-class)**
   - **[Exercise 4: Calculate GPA (Extended)](#exercise-4-calculate-gpa-extended)**

---

**[Session 4](#session-4)**
- **[Exercise 1: Counting Files in a Directory](#exercise-1-counting-files-in-a-directory)**
- **[Exercise 2: Validating File Names Against a Pattern](#exercise-2-validating-file-names-against-a-pattern)**
- **[Exercise 3: Counting Annotations per Month](#exercise-3-counting-annotations-per-month)**
- **[Exercise 4: Organizing Files into Monthly Folders](#exercise-4-organizing-files-into-monthly-folders)**
- **[Exercise 5: Sorting Annotations](#exercise-5-sorting-annotations)**
- **[Exercise 6: Identifying the Most Recent Annotation Satellite](#exercise-6-identifying-the-most-recent-annotation-satellite)**
- **[Exercise 7: Counting Unique Regions](#exercise-7-counting-unique-regions)**

---

## Folder Structure

<pre>
/
├── Screenshots/
│   ├── Session 1/
│   │   ├── Inputs/
│   │   │   └── screenshot_input_1.png
│   │   ├── Outputs/
│   │       └── screenshot_output_1.png
│   ├── Session 2/
│   │   ├── Inputs/
│   │   │   └── screenshot_input_2.png
│   │   ├── Outputs/
│   │       └── screenshot_output_2.png
│   ├── Session 3/
│   │   ├── Inputs/
│   │   │   └── screenshot_input_3.png
│   │   ├── Outputs/
│   │       └── screenshot_output_3.png
│   ├── Session 4/
│   │   ├── Inputs/
│   │   │   └── screenshot_input_4.png
│   │   ├── Outputs/
│   │       └── screenshot_output_4.png
│
├── Sessions/
│   ├── Session 1/
│   │   ├── Python Class 1.py
│   │   └── README.md
│   ├── Session 2/
│   │   ├── Python Class 2.py
│   │   └── README.md
│   ├── Session 3/
│   │   ├── Python Class 3.ipynb
│   │   └── README.md
│   ├── Session 4/
│   │   ├── Python Class 4.ipynb
│   │   └── README.md
</pre>

# **Session 1**

In Session 1, I learned the fundamental concepts of Python, including basic syntax, data types, and control structures. The exercises covered essential topics such as variables, arithmetic operations, string manipulation, and the use of lists, dictionaries, tuples, and sets.

## **List of exercises:**  

### **Exercise 1: Print a Greeting**
       
       - Write a Python program that prints a greeting message, such as "Hello, Python!".

**Description:** A program that prints a greeting message.

* **Input:** The program does not require user input. The output is predetermined.

![Input Greeting](Screenshots/Session%201/Inputs/Session1_Ex1_Inp_Greeting.png)

* **Output:** The output will display the greeting message "Hello, Python!".

![Input Greeting](Screenshots/Session%201/Outputs/Session1_Ex1_Out_Greeting.png)

---

### **Exercise 2: Basic Arithmetic**
       - Create a program that:
          - Defines two variables, `a` and `b`, with numerical values.
          - Prints their sum, difference, product, and quotient.

**Description:** A program that performs basic arithmetic operations on two numerical variables.

* **Input:** Two predefined variables, `a` and `b`, with values 10 and 2 respectively.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex2_Inp_Arithmetic..png)

* **Output:** The output will show the sum, difference, product, and quotient of `a` and `b`.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex2__Out_Arithmetic2_.png)

---

### **Exercise 3: String Manipulation**
       - Define a variable `name` and assign it your name. Write a program that prints a message saying "Hello, [name]!" where `[name]` is the value of the variable.

**Description:** A program that prints a message using a defined name variable.

* **Input:** A variable `name` assigned the value "Lucas".

![Input String](Screenshots/Session%201/Inputs/Session1_Ex3_Inp_String..png)

* **Output:** The output will display the message "Hello, Lucas!".

![Output String](Screenshots/Session%201/Outputs/Session1_Ex3_Out_String.png)

---

### **Exercise 4: Lists**
       - Create a list called `universities` with at least five different university names.
          - Print the entire list.
          - Print the first and last university in the list.

**Description:** A program that creates a list of universities and prints the first and last university.

* **Input:** A predefined list of universities.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex4_Inp_Lists..png)

* **Output:** The output will display the entire list and specify the first university as "UCC" and the last as "UTN".

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex4__Out_Lists_.png.png)

---

### **Exercise 5: Dictionaries**
       - Create a dictionary called `student` with keys: `name`, `age`, and `grade`, and assign appropriate values to each key.
       - Write a program that prints each key-value pair in the dictionary.

**Description:** A program that creates a dictionary of student information and prints each key-value pair.

* **Input:** A dictionary called `student` with keys: `name`, `age`, and `grade`.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex5_Inp_Dictionaries..png)

* **Output:** The output will show each key and its corresponding value from the dictionary.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex5_Out_Dic.png)

---

### **Exercise 6: Tuples**
       - Define a tuple called `coordinates` with two values representing a point in 2D space (e.g., `(x, y)`).
       - Print the value of `coordinates` and access each element by its index.

**Description:** A program that defines a tuple of coordinates and accesses each element by index.

* **Input:** A tuple `coordinates` assigned the values `(5, 10)`.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex6_Inp_Tuples.png)

* **Output:** The output will display the entire tuple and individual coordinates accessed by their indices.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex6_Out_Tuples.png)

---

### **Exercise 7: Sets**
       - Create a set called `colors` with the values: "red", "green", "blue".
       - Add another color to the set.
       - Try adding a duplicate color and observe what happens.
       - Print the set and remove one color from it.
       - Create another set named `light_colors` and merge `colors` and `light_colors`.

**Description:** A program that creates a set of colors, adds and removes elements, and prints the resulting set. It also demonstrates how sets handle duplicate entries and the union operation to combine two sets.

* **Input:** A predefined set of colors initialized with `{"red", "green", "blue"}`. The program adds the color `"black"` and attempts to add it again to observe how duplicates are managed. It also initializes another set, `light_colors`, with light color variants.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex7_Inp_Lists..png)

* **Output:** The program outputs the colors set after each operation, showing the effects of adding, removing, and merging sets.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex7_Out_Colors.png)

---

### **Exercise 8: Conditional Statements**
       - Write a program that:
         - Takes an input number from the user.
         - Checks if the number is positive, negative, or zero.
         - Prints an appropriate message based on the result.

**Description:** A program that checks if a user-input number is positive, negative, or zero.

* **Input:** A user-input number (for example, `-5`).

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex8_Inp_Cond..png)

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex8_Inp_Conditional.png)

* **Output:** The output will display whether the number is positive, negative, or zero.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex8_Out_Conditional.png)

---

### **Exercise 9: For Loop**
      - Create a list of numbers from 1 to 5.
      - Use a for loop to iterate through the list and print each number.

**Description:** A program that iterates through a list of numbers and prints each one using a for loop.

* **Input:** A predefined list of numbers: `[1, 2, 3, 4, 5]`.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex9_Inp_For_Loop..png)

* **Output:** The output will show each number printed on a new line.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex9_Out_For_Loop.png)

---

### **Exercise 10: While Loop**
      - Write a program that uses a while loop to print numbers from 1 to 5.
      - Ensure the loop terminates correctly.

**Description:** A program that prints numbers from 1 to 5 using a while loop.

* **Input:** The initial value for the loop is set to `1`.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex10_Inp_While_Loop..png)

* **Output:** The output will display the numbers from 1 to 5 printed sequentially.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex10_Out_While_Loop.png)

---

### **Exercise 11: Match Statement**
      - Write a program that:
      - Asks the user to input a grade (e.g., "A", "B", "C", "D", or "F").
      - Use a match statement to print a corresponding message for each grade:
          - "A": "Excellent!"
          - "B": "Good job!"
          - "C": "Fair."
          - "D": "Needs improvement."
          - "F": "Failing."
      - Handle invalid input by printing a default message.

**Description:** A program that takes a grade input from the user and prints a corresponding message using a match statement.

* **Input:** A user-input grade (for example, `"A"`).

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex11_Inp_Match..png)

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex11_Inp_Match.png)

* **Output:** The output will display "Excellent!" for grade "A".

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex11_Out_Match.png)

---

### **Exercise 12: Define a Function**
      - Write a function called `greet` that takes a name as an argument and prints "Hello, [name]!".
      - Call the function with your own name.

**Description:** A program that defines and calls a function to greet the user by name.

* **Input:** A variable `name` with the value `"Lucas"` passed to the function.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex12_Inp_Function.png)

* **Output:** The output will display the greeting message "Hello, Lucas!".

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex12_Out_Function.png)

---

### **Exercise 13: Function with Return Value**
      - Define a function called `square` that takes a number as an argument and returns its square.
      - Print the result of calling this function with different numbers.

**Description:** A program that defines a function to return the square of a number and prints the result.

* **Input:** A variable passed to the function (for example, `4`).

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex13_Inp_Return.png)

* **Output:** The output will display the squared value `16`.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex13_Out_Return.png)

---

### **Exercise 14: Function with Default Parameters**
      - Write a function called `multiply` that takes two parameters, `a` and `b`, and returns their product.
      - Set a default value of 1 for the parameter `b`.
      - Test the function with and without providing the second argument.

**Description:** A program that defines a function with default parameters and tests it with different arguments.

* **Input:** The function is called with one argument (for example, `3`).

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex14_Inp_Default.png)

* **Output:** The output will show the product of the arguments.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex14_Out_Default.png)

---

### **Exercise 15: List Comprehension**
      - Create a list of numbers from 1 to 10.
      - Use list comprehension to create a new list that contains the squares of these numbers.
      - Print the new list.

**Description:** A program that uses list comprehension to create a list of squares from 1 to 10.

* **Input:** The range of numbers is defined from `1 to 10`.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex15_Inp_ListC.png)

* **Output:** The output will display the list of squares.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex15_Out_ListC.png)

---

### **Exercise 16: Nested Data Structures**
      - Create a dictionary where the keys are names of students and the values are lists of their grades.
      - Write a function that takes the dictionary and prints the average grade for each student.

**Description:** A program that calculates and prints the average grade for each student from a dictionary of grades.

* **Input:** A predefined dictionary of students with their corresponding grades.

![Input Screenshot](Screenshots/Session%201/Inputs/Session1_Ex16_Inp_Nested.png)

* **Output:** The output will display the average grade for each student.

![Output Screenshot](Screenshots/Session%201/Outputs/Session1_Ex16_Out_Nested.png)

---

### **Exercise 17: Simple Calculator**
      - Write a program that:
          - Defines a function `calculate` which takes three parameters: two numbers and an operator (`+`, `-`, `*`, `/`).
          - Performs the operation and returns the result.
          - Ask the user for the two numbers and the operator, then call the function and print the result.

**Description:** This exercise involves creating a function called `calculate` that takes two numbers and an operator as input and performs the respective arithmetic operation (addition, subtraction, multiplication, or division).

**Input:**  
   - User provides two numbers (e.g., `10` and `5`).
   - User selects an arithmetic operator (`+`, `-`, `*`, or `/`).

![Simple Calculator Input](Screenshots/Session%201/Inputs/Session1_Ex17_Inp_Calculator.png)

![Simple Calculator Input](Screenshots/Session%201/Inputs/Session1_Ex17_Inp_Calculator1.png)

**Output:** The program prints the result of the chosen operation. For example, with input numbers `10` and `5`, and operator `+`, the output will be `15`.

![Simple Calculator Output](Screenshots/Session%201/Outputs/Session1_Ex17_Out_Calculator.png)

---

# **Session 2** 

In this session, I built upon the knowledge from Session 1, diving into more advanced topics like data filtering, function definitions, and practical applications.

## **List of exercises:** 

### **Exercise 1: FizzBuzz**
      
      - Write a FizzBuzz function that takes an integer `n` as a parameter.
      - Implement FizzBuzz logic to print:
          - "Fizz" for multiples of 3
          - "Buzz" for multiples of 5
          - "FizzBuzz" for multiples of both 3 and 5
          - The number itself for other numbers
      - Call the function for numbers 1 to 20.
      
* Description: Create a function that prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.

* Input: Numbers from 1 to 20.

![FizzBuzz Input](Screenshots/Session%202/Inputs/Session2_Ex1_Out_FizzBuzzz.png)
  
* Output: 

![FizzBuzz Output](Screenshots/Session%202/Outputs/Session2_Ex1_Out_FizzBuzz.png)

---

### **Exercise 2: Basic Data Filtering** 

      - Create a list that contains a mix of integers, strings, and floats.
      - Use list comprehension to create a new list that contains only the integers from the original list.
      - Print the filtered list of integers.
       
* Description: Filter a list that contains a mix of integers, strings and floats to extract only integers.

* Input: Mixed list

![Data Filtering Input](Screenshots/Session%202/Inputs/Session2_Ex2_Inp_DataFiltering.png)
  
* Output:

![Data Filtering Output](Screenshots/Session%202/Outputs/Session2_Ex2_Out_DataFiltering.png)

---

### **Exercise 3: Simple To-Do List** 

      - Create an empty list called `todo_list`.
      - Define functions:
          - `add_task(task)` that adds a task to the list.
          - `show_tasks()` that prints all tasks in the list.
          
* Description: Create a simple to-do list application with functions to add and show tasks.

* Input: Tasks to add and an input to show the current tasks. 

![To do list Input](Screenshots/Session%202/Inputs/Session2_Ex3_Inp_ToDoList..png)
  
* Output:

![To do list Output](Screenshots/Session%202/Outputs/Session2_Ex3_Out_ToDoList.png)

---

### **Exercise 4: Temperature Converter** 
      
      - Write a function `celsius_to_fahrenheit(celsius)` that converts Celsius to Fahrenheit.
      - Print the converted temperature for 22ºC, 46ºC, 51ºC, and 76ºC.

* Description: Create a function that converts Celsius into Fahrenheit.

* Input: Different Celsius values (22ºC, 46ºC, 51ºC, and 76ºC).

![Temperature Converter Intput](Screenshots/Session%202/Inputs/Session2_Ex4_Inp_Temperature..png)
  
* Output:

![Temperature Converter Output](Screenshots/Session%202/Outputs/Session_2_Ex4_Temperature_converter.png)


---

# **Session 3** 

In Session 3, I explored object-oriented programming concepts in Python. This session focused on defining classes, managing attributes, and implementing methods. The exercises revolved around creating a simple course registration system that allows students to enroll in courses and manage their registrations.

## **List of exercises:** 

### **Exercise 1: Course Class**

         - Create a **Course** class, where each course has a name, a description and a list of enrolled students. You'll need to implement the next methods:
            - Add a student to the course.
            - Remove a student from the course.
            - Show all students in the course.

* Description: A class representing a course with methods to manage students enrolled in the course.

* Input:

   - Course details such as:
      - name: "Python Programming"
      - course_type: "Online"
      - Description: "Learn the fundamentals of Python programming."

![Course_Class_Input](Screenshots/Session%203/Inputs/Session3_Ex1_Inp3.png)

![Course_Class_Input](Screenshots/Session%203/Inputs/Session3_Ex1_Inp2.png)

* Output:

![Course_Class_Output](Screenshots/Session%203/Outputs/Session3_Ex1_Out.png)

---

### **Exercise 2: Student Class**

      - Create a **Student** class, where each student has a name, ID number, address and a list of enrolled courses with the following methods:
         - Enroll in a course.
         - Drop a course.
         - Show all registered student courses.

* Description: A class representing a student with methods to show student information.

* Input:

   - Student details such as:
      - Name: "Lucas Brunengo"
      - ID: "LB0202"


![Course_Student_Input](Screenshots/Session%203/Inputs/Session3_Ex2_Inp.png)

![Course_Student_Input](Screenshots/Session%203/Inputs/Session3_Ex2_Inp2.png)

* Output:

![Course_Student_Output](Screenshots/Session%203/Outputs/Session3_Ex2_Out.png)

---


### **Exercise 3: Registration Class**

      - Create a central class that manages courses and students, **Registration** class, where you have a list of students and a list of courses, and methods:
          - Enroll in a course.
          - Drop a course.
          - Show all the enrolled courses.
          - Show all the students.

* Description: A class representing a registration system for managing courses.

* Input:

   - Course object to add to the registration system.

![Course_Registration_Input](Screenshots/Session%203/Inputs/Session3_Ex3_Inp.png)

![Course_Registration_Input](Screenshots/Session%203/Inputs/Session3_Ex3_Inp2.png)

![Course_Registration_Input](Screenshots/Session%203/Inputs/Session3_Ex3_Inp3.png)

![Course_Registration_Input](Screenshots/Session%203/Inputs/Session3_Ex3_Inp4.png)

* Output:

![Course_Registration_Output](Screenshots/Session%203/Outputs/Session3_Ex3_Out.png)

---

### **Exercise 4: Calculate GPA (Extended)**

      - Let's add grades to each student's course and create method that yields the GPA given a student name or ID.

* Description: A method added to the Course class that calculates the average GPA of enrolled students.

* Input:

![Course_gpa_Output](Screenshots/Session%203/Inputs/Session3_Ex4_Inp.png)

![Course_Registration_Input](Screenshots/Session%203/Inputs/Session3_Ex4_Inp2.png)

![Course_Registration_Input](Screenshots/Session%203/Inputs/Session3_Ex4_Inp3.png)

![Course_Registration_Input](Screenshots/Session%203/Inputs/Session3_Ex4_Inp4.png)

![Course_Registration_Input](Screenshots/Session%203/Inputs/Session3_Ex4_Inp5.png)

![Course_Registration_Input](Screenshots/Session%203/Inputs/Session3_Ex4_Inp6.png)

* Output:

![Course_gpa_Output](Screenshots/Session%203/Outputs/Session3_Ex4_Out.png)

---

# **Session 4** 

In Session 4, I explored object-oriented programming concepts in Python. This session focused on defining classes, managing attributes, and implementing methods. The exercises revolved around creating a simple course registration system that allows students to enroll in courses and manage their registrations.

## **List of exercises:** 

### **Exercise 1: Counting files in a directory**

      - How many files the annotations folder has.

* Description: This exercise counts the total number of files in a specified annotations directory and prints the count.

* Input:

![Course_gpa_Output](Screenshots/Session%204/Inputs/Session4_Ex1_Inp.png)

* Output:

![Course_gpa_Output](Screenshots/Session%204/Outputs/Session4_Ex1_Out.png)

---

### **Exercise 2: Validating File Names Against a Pattern**
      - {DATE}_{TIME}_SN{SATELLITE_NUMBER}_QUICKVIEW_VISUAL_{VERSION}_{UNIQUE_REGION}.txt

         where:

            - DATE expressed as YYYYMMDD (year, month and day), e.g. 20241201, 20230321 ...
            - TIME expressed as HHMMSS (hour, minutes and seconds), e.g. 2134307
            - SATELLITE_NUMBER an integer that represents the satellite number.
            - VERSION provides the version of the pipeline, e.g. "0_1_2", "1_3_1" ...
            - UNIQUE_REGION provides a unique location in the form of a string, e.g SATL-2KM-10N_552_4164
            
      - How many of them follow the name convention expressed above. 

* Description: This exercise filters files based on a specific naming convention, counts valid and invalid files, and prints the results.

* Input:

![Course_gpa_Output](Screenshots/Session%204/Inputs/Session4_Ex2_Inp.png)

* Output:

![Course_gpa_Output](Screenshots/Session%204/Outputs/Session4_Ex2_Out.png)

---

### **Exercise 3: Counting Annotations per Month**

      - How many of annotations you have per month and year. Which month has more annotation files.

* Description: This exercise counts the number of annotations per month from valid files, tracks satellite counts, and finds the month with the most annotations.

* Input:

![Course_gpa_Output](Screenshots/Session%204/Inputs/Session4_Ex3_Inp.png)

![Course_gpa_Output](Screenshots/Session%204/Inputs/Session4_Ex3_Inp1.png)
* Output:

![Course_gpa_Output](Screenshots/Session%204/Outputs/Session4_Ex3_Out.png)

---

### **Exercise 4: Organizing Files into Monthly Folders**

      - Create a new annotations folder with multiple folders corresponding to a month.

* Description: This exercise organizes valid annotation files into subfolders based on their respective months.

* Input:

![Course_gpa_Output](Screenshots/Session%204/Inputs/Session4_Ex4_Inp.png)

* Output:

![Course_gpa_Output](Screenshots/Session%204/Outputs/Session4_Ex4_Out.png)

![Course_gpa_Output](Screenshots/Session%204/Outputs/Session4_Ex4_Out1.png)

---

### **Exercise 5: Sorting Annotations**

      - Print all the annotations from the most recent to the oldest one. 

* Description: This exercise sorts valid annotation files by date and time in descending order and prints them.

* Input:

![Course_gpa_Output](Screenshots/Session%204/Inputs/Session4_Ex5_Inp.png)

* Output:

![Course_gpa_Output](Screenshots/Session%204/Outputs/Session4_Ex5_Out.png)

---

### **Exercise 6: Identifying the Most Recent Annotation Satellite**

      - How many different satellites there are, how many annotations we have per satellite number, and which one was used in the most recent annotation file. 

* Description: This exercise identifies the satellite of the most recent annotation and prints the result.

* Input:

![Course_gpa_Output](Screenshots/Session%204/Inputs/Session4_Ex6_Inp.png)

* Output:

![Course_gpa_Output](Screenshots/Session%204/Outputs/Session4_Ex6_Out.png)

---

### **Exercise 7: Counting Unique Regions**

      - How many unique regions there are.

* Description: This exercise counts the number of unique regions identified from the valid annotation files.

* Input:

![Course_gpa_Output](Screenshots/Session%204/Inputs/Session4_Ex7_Inp.png)

* Output:

![Course_gpa_Output](Screenshots/Session%204/Outputs/Session4_Ex7_Out.png)



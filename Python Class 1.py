#Excercise 1

greeting = ("Hello, Python")
print(greeting)

#Excercise 2

a = 10
b = 2

summarize = (a + b) 
diff = (a - b)
product = (a * b)
quotient = (a / b)

print(sum) 
print(diff)
print(product)
print(quotient)


#Excercise 3
name = "Lucas"
print(f"Hello, {name}!")


#Excercise 4

universities = ["UCC", "ESADE", "UBA", "UNC", "UTN"]
print(universities)
print(universities[0] + " " + universities[4])


#Excercise 5

student = {
            "Lucas" : {
                "age" : 24, 
                "grade" : 10 
                },
            "Manuel" : {
                "age" : 17,
                "grade" : 9
                },
            }

print(student)


#Excercise 6

coordinates = (5,10)

print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])


#Excercise 7

colors = {"red", "green", "blue"}
colors.add("black")
print(colors)

colors.add("black")
print(colors)

colors.remove("black")
print(colors)

light_colors = {"light_red", "light_green", "light_blue"}
print(light_colors)

merged_colors = colors.union(light_colors)
print(merged_colors)


#Excercise 8

EX8 = int(input("Enter a number: "))

if EX8 > 0 :  
    print("The number is positive!")
elif EX8 < 0 :
    print("The number is negative!")
else :   
    print("The number is 0!")


#Excercise 9

List_1 = [1, 2, 3, 4, 5]

for number in List_1 : 
    print(number)
else : 
    print("All numbers have been printed!")


#Excercise 10

counter = 1

while counter <= 5: 
    print(counter)
    counter += 1
else : 
    print("Loop Finished!")


#Excercise 11

grade = input("Enter a grade: ").upper()

if grade == "A" :
    print("Excellent")
elif grade == "B" :
    print("Good Job")
elif grade == "C" :
    print("Fair")
elif grade == "D" :
    print("Needs Improvement")
elif grade == "F" :
    print("Failing")
else :
    print("Invalid Input. Enter a valid grade (A, B, C, D, F)")


#Excercise 12

def greet(name) : 
    print(f"Hello, {name}")

greet("Lucas")


#Excercise 13

def square(number) :
    return number ** 2

print(square(2))
print(square(3))
print(square(4))
print(square(5))

#Excercise 14

def multiply(a, b = 1) :
    return a * b

print(multiply(3))


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


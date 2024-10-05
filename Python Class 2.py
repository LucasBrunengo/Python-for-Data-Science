#Excersice 1

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


#Excersice 2

Mixed_List = ["Lucas", 24, 24.7, "Agustin", 27, 27.9, "Manuel", 18, 18.1]

Int_List = [x for x in Mixed_List if isinstance(x, int)]

print(Int_List)


#Exercise 3

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

#Excercise 4

def celsius_to_fahrenheit(celsius) :
    return (celsius * 1.8) + 32

print(f"22ºC equals to {celsius_to_fahrenheit(22)}ºF")
print(f"46ºC equals to {celsius_to_fahrenheit(46)}ºF")
print(f"51ºC equals to {celsius_to_fahrenheit(51)}ºF")
print(f"76ºC equals to {celsius_to_fahrenheit(76)}ºF")

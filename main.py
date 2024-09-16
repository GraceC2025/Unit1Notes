def main():
    # declare variables 
    age = 17
    teacher = "Ms. Navab"
    is_Class = True
    grade = 99.99

    # check the type of variable
    type_Of_Age = type(age)
    print(type_Of_Age)

    # string formatting (f-strings vs commas)
    print(f"The type of the variable age is: {type_Of_Age}")
    print("The type of the variable age is:", type_Of_Age)

    x = 42
    y = 3 / 4
    z = int('7')
    a = float(5)
    name = "Nina"

    # (can nest the type function in print)
    print(type(x))
    print(type(y))
    print(type(z))
    print(type(a))
    print(type(name))

    # math in f-strings
    print(f"My age in 10 years: {age + 10}", end="\n \n")

    # initialize args for function
    ingredients_List = ["chocolate chips", "cinnamon", "flour", "sugar", "butter", "eggs"]
    baking_Instructions = "Mix everything together and put into oven"
    oven_Temp = 325 

    # call a function
    bake_Cookie(ingredients_List, baking_Instructions, oven_Temp)

    #call function with optional args
    bake_Cookie(ingredients_List, baking_Instructions, oven_Temp, "star")

    # call second function
    print(calculate_Numbers(2, 3))
    print(calculate_Numbers(2, 3, "subtract"))
    print(calculate_Numbers(2, 3, operation = "subtract"))

    # demonstrate modifying values while iteratiing
    numbers = [5, 5, 6, 5.5, 7, 42, 70, "hi"]
    list_Iteration(numbers)

    # test different container types
    list_Demo()
    tuple_Demo()
    set_Demo()
    dict_Demo()

def list_Demo():
    print("LIST DEMO")
    new_List = ["h", "e", "l", "l", "o"]

    # add item to list
    new_List.append("!")

    print(new_List)
    print(len(new_List))

    # use index to access items
    print(new_List[0])
    print(new_List[4:6]) # (last number not inclusive)
    print(new_List[4:]) # same as 4:6 (everything onwards)
    print(new_List[-2:]) # accessing index counting backwards/neg

    # remove an item
    new_List.remove("l") # (refers to first l)

    # insert an item
    new_List.insert(1, "l")
    print(new_List)

def tuple_Demo():
    print("TUPLE DEMO")

def set_Demo():
    print("SET DEMO")

def dict_Demo():
    print("DICT DEMO")

def bake_Cookie(ingredients, instructions, temperature, cutter = "circle"):
    # print the list of ingredients
    for item in ingredients:
        print(item)

    # print the oven temperature setting
    print(f"Set oven temperature to: {temperature}")

    # print the instructions
    print(instructions, end="\n")
    
    #print which cookie cutter to use
    print(f"Feel free to use a {cutter} cookie cutter before baking", end="\n \n")

def calculate_Numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    
def list_Iteration(list):
    # create a new list as you loop
    new_List = []
    for item in list:
        new_List.append(item * 2)
    print(new_List)

    # list comprehension
    input_List = [item * 2 for item in list]
    print(input_List)

if __name__ == "__main__":
    main()



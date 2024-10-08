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
    print()
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
    print(new_List)

    # insert an item
    new_List.insert(1, "l")
    print(new_List)

    # check if a value exists
    print("!" in new_List)

    # sort list (reverse alphabetical order example)
    new_List.sort(reverse=True)
    print(new_List, end="\n \n")

def tuple_Demo():
    print("TUPLE DEMO")

    # tuples are immutable (lowkey suck)
    person = ("Courtney", 17, "Brooklyn")
    name, age, hometown = person 
    print(name)
    print(age)
    print(hometown, end="\n \n")

def set_Demo():
    print("SET DEMO")

    new_Set = set()
    new_Set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    # sets are mutable
    new_Set.add(0) # will insert in order
    new_Set.remove(4)
    print(new_Set)
    
    new_Set.add(8) # will not add b/c wont repeat a value
    print(new_Set)

    # math operations between two sets
    second_Set = {2, 4, 6, 8, 10}
    print(new_Set.union(second_Set))
    print(new_Set.intersection(second_Set))
    print(new_Set.difference(second_Set), end="\n \n")

def dict_Demo():
    print("DICT DEMO")
    # create a dictionary with values {key: value}
    # dictionary inside of a dictionary
    costumes = {
        "M&M": {"popularity %": 0.40, "school appropriate": True, "items": ["suit", "white tights"]},
        "Cat": {"popularity %": 0.95, "school appropriate": "Maybe", "items": ["ears"]},
        "Jorge": {"school appropriate": False, "items": ["clown hammer"]}
    }
    print(costumes, end="\n \n")
    print(costumes.items(), end="\n \n")
    print(costumes.keys(), end="\n \n")
    print(costumes.values(), end="\n \n")

    # how to access items
    print(costumes["Jorge"])
    print(costumes.get("Cat"))
    print("Mr. Titcomb" in costumes, end="\n \n") # gives false b/c doesn't exist

    # how to add items
    costumes["Mr. Titcomb"] = {"popularity %": 1.00, "school appropriate": True}

    # iterate through dictionary
    print("Iterate Through Dictionary:")
    for costume in costumes:
        print(costume)
        print(costumes[costume])

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



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

if __name__ == "__main__":
    main()

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
    print(f"My age in 10 years: {age + 10}")

def bake_Cookie(ingredients, temperature, instructions):
    # print the list of ingredients

    # print the oven temperature setting
    

    # print the instructions
    print(instructions)

if __name__ == "__main__":
    main()

#Write a function called add_vals() that adds
# Write the function so that if num1 is bigger than num2
# it displays num3, otherwise it says invalid input

def add_vals(num1, num2, num3):
    if num1 > num2:
        print(num3)
    else:
        print("Invalid input.")

add_vals(3, 4, 7)
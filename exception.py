name = input("What is your name ? ")
age = input("How old are you ? ")

print("Hello, " , name, "!", sep="" )

try:
    age = int(age) # convert string to integer
    birth_year = 2023 - age
    print(name, " you were born in ", birth_year, ".", sep="")
    number = input("give me a number to divide the age")
    number = int(number)
    print(age / number)

except ValueError:
    print("invalid age. Please enter a number")

except ZeroDivisionError:
    print("you cannot divide by zero")

else:
    print("no exceptions were raised")

finally:
    print("thank you for playing")


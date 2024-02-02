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

except:
    print("some other error i did not foresee")

else:
    print("no exceptions were raised")

finally:
    print("thank you for playing")

try:
    name = input("What is your name?")
    age = input("How old are you?")
    age = int(age) #convert string to integer


except ValueError:
    print("Invalid age. Please enter a number.")


else:
    if age < 0 or age > 140
        drinks = ("vodka", "tequila", "gin")

elif age > 120:
        print("You are too old to play the awesome drinking game.")

elif age < 18:
        print("You are a minor. You can not play the awesome drinking game.")

elif (country == "USA" or country == "UAE") and age < 21
        print( )

else:
        print("You are an adult. You can play the awesome drinking game.")
        print("Have some", random.choice(drinks), "and enjoy the game.")
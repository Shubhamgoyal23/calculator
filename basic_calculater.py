# 1. username and password login
# 2. user se caluleter ke oprenaton option chose
# 3. result print 

# step1

predifine_username= "shubham_goyal"
predifine_password= 2020215

# # login
username = input("Enter your username:")
password = int(input("Enter your password:"))

if username == predifine_username:
    if password == predifine_password:
        print("Welcome user (how's your day)")
    else:
        print("Invelid password\ntry again")
else:
    print("Invelid username\ntry again")


# step 2
# creat a calculetrer

# +
def add2num(num1, num2):
    return num1 + num2

# -
def sub2num(num1, num2):
    return num1 - num2

# *
def multi2num(num1, num2):
    return num1 * num2

# /
def divide2num(num1, num2):
    return num1 / num2

# user se option choice

print("Please select a operation:\n"
      "1. Addition [+]\n"
      "2. Substraction [-]\n"
      "3. Multiplication [*]\n"
      "4. Division [/]\n")

select = int(input("Select the operation from [1],[2],[3],[4]:"))

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

# final result

if select == 1:
    print(f"{number1}+{number2} = {add2num(number1, number2)}")
elif select == 2:
    print(f"{number1}-{number2} = {sub2num(number1, number2)}")
elif select == 3:
    print(f"{number1}*{number2} = {multi2num(number1, number2)}")
elif select == 4:
    print(f"{number1}/{number2} = {divide2num(number1, number2)}")
else:
    print("INVELID OPERATION SELECTED\n please try again")

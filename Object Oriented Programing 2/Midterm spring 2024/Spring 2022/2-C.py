# Taking input from the user
user_input = input("Enter a list: ")

# Converting the user input to a list
#user_list = eval(user_input)
user_input =[value for value in user_input]

# Checking if there are enough elements in the list
if len(user_input) < 3:
    print("Not possible")
else:
    # Creating a new list excluding the first and last elements
    new_list = user_input[1:-1]
    print(new_list)




############# Convert To List User Input
number_string =input("Enter Number ->>")
#number_string = "123456789"12
number_list =[(num) for num in number_string]
print(number_list)


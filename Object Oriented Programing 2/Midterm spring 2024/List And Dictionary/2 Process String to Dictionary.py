user_input =input("Enter any type of String --->>")

my_list =[num for num in user_input]
#print(my_list)

# Then  convert into dictionary

my_dict ={key : value for key , value in enumerate(my_list)}
print(my_dict)
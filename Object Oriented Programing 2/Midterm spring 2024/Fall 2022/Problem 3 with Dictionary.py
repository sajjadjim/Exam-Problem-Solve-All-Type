user_dict = {}
num_user = int(input("Enter number of user ->"))

for i in range(1 ,num_user+1):
    name = input(f"Enter user {i} name :")
    plan = input(f"Enter user {i} plan (Basic / Standard / Premium ) :")

    if plan == "Basic":
        bill = 9.99
    elif plan == "Standard":
        bil = 15.99
    elif plan == "Premium":
        bill = 19.99

    else:
        print(f"User {i} don't select any Bill !!")

    user_dict[i]= {"name" :name , "plan" : plan ,"bill" : bill}

print("\nBill of all User ->>")
for user_serial , user_info in user_dict.items():
        print(f"User. {user_serial}->{user_info["name"]} ",
              f" Plan->{user_info["plan"]}"
              f" Payment->{user_info["bill"]}"
              )


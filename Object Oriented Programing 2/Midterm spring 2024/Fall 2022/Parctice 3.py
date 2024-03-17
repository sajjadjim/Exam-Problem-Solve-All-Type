def user_payment_system():
    #Initialization the dictionary Storage
    users_dict = {}
    num_users=int(input("Enter the Number of user ->"))

    for i in range(1, num_users + 1):
        name = input(f"Enter the name of user {i}: ")
        plan = input(f"Enter the preferred plan for user {i} (Basic/Standard/Premium): ")

        # Determine the monthly payment based on the plan
        if plan == "Basic":
            payment = 9.99
        elif plan == "Standard":
            payment = 15.99
        elif plan == "Premium":
            payment = 19.99
        else:
            print("Invalid plan! Please choose from Basic, Standard, or Premium.")
            continue

        # Insert user information into the dictionary
        users_dict[i] = {"name": name, "plan": plan, "payment": payment}

    print("User Information :")
    for user_serial ,user_info in users_dict.items():
        print(f"User {user_serial}: {user_info['name']}, Plan: {user_info['plan']}, Payment: ${user_info['payment']}")



user_payment_system()
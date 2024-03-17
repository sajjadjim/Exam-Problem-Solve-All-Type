def insert_payment():
    # Initialize an empty dictionary to store user information
    user_dict = {}

    # Taking user input for the number of users
    num_users = int(input("Enter the number of users: "))

    # Taking user input for each user's name and preferred plan
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
        user_dict[i] = {"name": name, "plan": plan, "payment": payment}

    # Print the nested dictionary
    print("User Information:")
    for user_id, user_info in user_dict.items():
        print(f"User {user_id}: {user_info['name']}, Plan: {user_info['plan']}, Payment: ${user_info['payment']}")

# Call the function to insert payments and print user information
insert_payment()

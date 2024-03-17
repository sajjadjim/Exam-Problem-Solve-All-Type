num =[101, 102 , 103 , 104 ,105]
name =["Sajjad" , "Hossain" , "Jim" , "Siam"]

value = list(zip(num,name ,"1234"))
print(value)


def lists_to_dict(num, country):
    # Check if the length of both lists are the same
    if len(num) != len(country):
        return None  # Return None if the lists are of different lengths

    # Use zip() to combine the two lists into a dictionary
    result_dict = dict(zip(num, country))
    return result_dict

# Define the lists
K = [1001, 1002, 1003, 1004 , 1005]
V = ["USA", "Canada", "China", "Japan", "UK"]

# Convert the lists into a dictionary
result_dict = lists_to_dict(K, V)

# Print the resulting dictionary
print(result_dict)


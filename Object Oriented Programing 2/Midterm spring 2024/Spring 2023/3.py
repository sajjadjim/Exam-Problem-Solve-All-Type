def lists_to_dict(keys, values):
    # Check if the length of both lists are the same
    if len(keys) != len(values):
        return None  # Return None if the lists are of different lengths

    # Use zip() to combine the two lists into a dictionary
    result_dict = dict(zip(keys, values))
    return result_dict


# Define the lists
K = [1001, 1002, 1003, 1004, 1005]
V = ["USA", "Canada", "China", "Japan", "UK"]

# Convert the lists into a dictionary
result_dict = lists_to_dict(K, V)

# Print the resulting dictionary
print(result_dict)

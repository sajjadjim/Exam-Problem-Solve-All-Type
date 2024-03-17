def string_to_dict(input_string, delimiter=','):
    # Split the string into key-value pairs based on the delimiter
    pairs = input_string.split(delimiter)

    # Initialize an empty dictionary
    result_dict = {}

    # Iterate over the key-value pairs
    for pair in pairs:
        # Split each pair into key and value
        key, value = pair.split(':')

        # Add key-value pair to the dictionary
        result_dict[key.strip()] = value.strip()

    return result_dict


# Example usage:
input_string = "key1:value1, key2:value2, key3:value3"
result = string_to_dict(input_string)
print(result)


def string_to_dict(input_string, delimiter=','):
    # Split the string into key-value pairs based on the delimiter
    pairs = input_string.split(delimiter)

    # Initialize an empty dictionary
    result_dict = {}

    # Iterate over the key-value pairs
    for pair in pairs:
        # Split each pair into key and value
        key, value = pair.split(':')

        # Add key-value pair to the dictionary
        result_dict[key.strip()] = value.strip()

    return result_dict


# Take user input for the string
input_string = input("Enter the string of key-value pairs (e.g., key1:value1, key2:value2): ")

# Call the function with user input
result = string_to_dict(input_string)
print(result)

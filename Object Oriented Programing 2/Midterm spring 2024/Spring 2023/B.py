#b) Develop a function to regenerate the values in reverse and sorted order:

data_str = "181,178,187,182,192,189,202,201"

# Convert the string to a list of integers
data_list = [int(num) for num in data_str.split(",")]

def regenerate_data(data):
    # Reverse the list
    reversed_data = data[::-1]
    # Sort the reversed list
    sorted_data = sorted(reversed_data)
    return sorted_data

# Call the function with the provided dataset
sorted_reversed_data = regenerate_data(data_list)

print("\nRegenerated data (reversed and sorted):",sorted_reversed_data)


# Define the list of temperatures
temperatures = [22, 18, 25, 20, 17, 23, 21]
# Question i solve ->
print("Original list of temperatures:", temperatures)


# Question ii solve ->
low_temp= temperatures.index(min(temperatures))
high_temp =temperatures.index(max(temperatures))

# Swap Operation
temperatures[low_temp], temperatures[high_temp] = temperatures[high_temp], temperatures[low_temp]

# Question 3 Solve ->After Print swap
print("Temperature after swap operation:", temperatures)


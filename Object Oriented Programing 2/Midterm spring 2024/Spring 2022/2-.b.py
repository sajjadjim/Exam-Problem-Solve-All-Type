# Define Two List

List1 = [1, 2, 3]
List2 = [2, 4, 6]

# print (List1 & List2)
common_elements = []

for element in List1:
    if element in List2:
        common_elements.append(element)

if common_elements:
        print(f"Common elements : {common_elements}")
else:
        print("No elements is common exsist !!!")

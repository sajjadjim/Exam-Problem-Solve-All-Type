
def find_common_elements_and_create_dict(list1, list2):
    common_elements = [num for num in list1 if num in list2]
    result_dict = {num: num ** 3 for num in list1}
    return common_elements, result_dict

list1 = [11, 13, 17, 19, 23]
list2 = [3, 6, 9, 12, 15]

common_elements, result_dict = find_common_elements_and_create_dict(list1, list2)
print("Common Elements:", common_elements)
print("Result Dictionary:", result_dict)


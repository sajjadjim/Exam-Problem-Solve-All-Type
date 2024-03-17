number_string = "123456789"
number_list =[(num) for num in number_string]
print(f"String to List convert->>{number_list}")

convert_dict = {key : value for key , value in enumerate(number_list)}
print(f"List value convert to Dictionary ---->{convert_dict}")
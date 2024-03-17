#Another One
def convert (Fahreheit):
    return (Fahreheit -32)*(5/9)

fahrenheit_temps = [100, 110, 120 ,130 ,140 ,150]
convert_value =list(map(convert,fahrenheit_temps))
print(f"Celsius_temps={convert_value}")








#ANother One
celsius_temps = [100, 110, 120, 130, 140, 150]
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))

print(fahrenheit_temps)

# No1
def convert_temperature(value, unit):
    if unit == 'C':
        result = (value * 9 / 5) + 32
    else:
        result = (value - 32) * 5 / 9
    return round(result, 2)

print("Celsius ke Fahrenheit : ", convert_temperature(100, 'C'))
print("Fahrenheit ke Celsius : ", convert_temperature(212, 'F'))

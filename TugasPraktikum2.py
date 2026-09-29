def convert_temperature(value, unit):
    "Convert temperature: C -> F or F -> C"
    if unit == 'C':
        result = (value * 9 / 5) + 32
    else:
        result = (value - 32) * 5 / 9
    return round(result, 2)

#No2
from math import pi

luas = lambda r: pi * r ** 2

print("Luas lingkaran : ", round(luas(7), 2))


# Function dari function
def jalankan(func, value):
    return func(value)
print("100 C ke F     : ", jalankan(lambda c: convert_temperature(c, 'C'), 100))
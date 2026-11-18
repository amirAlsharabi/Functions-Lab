# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.


def calculate_area_triangle(base, height):
    area = (base * height) / 2
    return area


print("Exercise 1:", calculate_area_triangle(10, 5))


print("------------------------")


# Exercise 2: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.


def apply_discount(price, discount_percentage):
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount


print("Exercise 2:", apply_discount(100, 25))


print("------------------------")


# Exercise 3: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.
def convert_temperature(temp, unit):
    if unit == "C":
        return (temp * 9 / 5) + 32
    elif unit == "F":
        return (temp - 32) * 5 / 9


print("Exercise 3: Convert 0°C to Fahrenheit:", convert_temperature(0, "C"))
print("Exercise 3: Convert 32°F to Celsius:", convert_temperature(32, "F"))


print("------------------------")


# Exercise 4: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.


def sum_to(n):
    total = 0
    for number in range(1, n + 1):
        total += number
    return total


print("Exercise 4:", sum_to(6))

print('------------------------')


# Exercise 5: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.
def largest(num1 , num2 , num3):
    return max(num1,num2,num3)


print('Exercise 5:', largest(1, 2, 3))

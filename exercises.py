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

print("------------------------")


# Exercise 5: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.
def largest(num1, num2, num3):
    return max(num1, num2, num3)


print("Exercise 5:", largest(1, 2, 3))


print("------------------------")


# Exercise 6: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.
def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * (tip_percentage / 100)


print("Exercise 6:", calculate_tip(50, 20))


print("------------------------")


# Exercise 7: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.
def product(*args):
    total - 1
    for num in args:
        total *= num
    return total


print("Exercise 7:", product(2, 5, 5))

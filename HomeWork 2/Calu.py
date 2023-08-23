import math
# Calculate the perimeter and area of a circle
def calculate_circle(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return perimeter, area

# Calculate the perimeter and area of a rectangle
def calculate_rectangle(length, width):
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area

# Calculate the perimeter and area of a square
def calculate_square(side):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area

# Get user input for circle radius
radius = float(input("Enter the radius of the circle: "))

# Calculate circle perimeter and area
circle_perimeter, circle_area = calculate_circle(radius)
print("Circle Perimeter:", circle_perimeter)
print("Circle Area:", circle_area)

# Get user input for rectangle dimensions
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate rectangle perimeter and area
rectangle_perimeter, rectangle_area = calculate_rectangle(length, width)
print("Rectangle Perimeter:", rectangle_perimeter)
print("Rectangle Area:", rectangle_area)

# Get user input for square side length
side = float(input("Enter the side length of the square: "))

# Calculate square perimeter and area
square_perimeter, square_area = calculate_square(side)
print("Square Perimeter:", square_perimeter)
print("Square Area:", square_area)

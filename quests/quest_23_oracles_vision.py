# Quest 23: The Oracle's Vision
# Concept: Functions that return a value instead of just printing one.

def calculate_area(length, width):
    area = length * width
    return area  # the function hands the result back to whoever called it

# Call it for two different rectangles
area_1 = calculate_area(5, 3)
area_2 = calculate_area(10.5, 2)

print(f"The first rectangle has an area of {area_1}.")
print(f"The second rectangle has an area of {area_2}.")

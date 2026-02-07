import math

def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height * width) / cover)
    return num_of_cans

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

print(f"You'll need {paint_calc(height=test_h, width= test_w, cover = coverage)} cans of paint.")
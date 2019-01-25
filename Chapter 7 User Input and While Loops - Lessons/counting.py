# Introducting while loops, p.122

current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

# Code above: the while loop set a condition that if current_number <= to 5,
# then print the number. Lane 7 adds 1 to current_number and the loop
# repeats itself until we get to number 5. The loop stops when value of
# current_number is 6.

print('\n')

# Using continue in a loop, p.126


current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Code Above, rough translation: while number is less than 10, add 1 to current
# number. If the current number is a multiple of two, the loop continues and
# the rest (print statement ln.25) gets ignored. If number is NOT a multiple of
# 2, then it gets printed and the loop continues until we reach 10.

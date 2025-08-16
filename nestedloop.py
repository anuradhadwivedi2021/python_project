 
#Nested loop matlab ek loop ke andar doosra loop.
#Har baar outer loop chalega, uske andar ka inner loop poora run hoga.
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} x {j} = {i*j}")
    print("---- End of table ----")

#star pattern
for i in range(1, 6):  # Outer loop → rows
    for j in range(i):  # Inner loop → stars
        print("*", end="")
    print()  # New line after each row


#While + For Combination
#row = 1
while row <= 3:  # Outer loop
    for col in range(1, 4):  # Inner loop
        print(f"Row {row}, Col {col}")
    row += 1

#simple grid
for row in range(1, 4):  # Outer loop → rows
    for col in range(1, 4):  # Inner loop → columns
        print(f"({row},{col})", end=" ")
    print()  # New line after each row

#number pattren
for i in range(1, 5):  # Outer loop → rows
    for j in range(1, i+1):  # Inner loop → numbers in each row
        print(j, end=" ")
    print()  # New line after each row

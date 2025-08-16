#PROBLEM 1
# #Write a program to find a sum of all the even numbers up to 50."""

sum = 0
for i in range(1, 51):   # 2 se 50 tak even numbers
    sum += i
print("Sum of even numbers up to 50 is:", sum)





#PROBLEM2
#WRITE A PROGRAM TO WRITE FIRST 20 NUMBER THIER SQUARED NUMBERS
for i in range(1, 21):
    print(i, "squared is", i**2)






#PROBLEM 3
#WRITE A PROGRAM TO FIND SUM OF FIRST 10 ODD NUMBER USING WHILE LOOP
count = 0
num = 1
sum_odd = 0

while count < 10:
    sum_odd += num
    num += 2
    count += 1

print("Sum of first 10 odd numbers is:", sum_odd)








#PROBLEM 4
#WRITE A PROGRAM TO CHECK IF A NUMBER IS DIVISIBLE BY 8 AND 100 NUMBERS

for i in range(1, 101):
    if i % 8 == 0:
        print(i, "is divisible by 8")



#PROBLEM 5
# WRITE A PROGRAM TO CREATE A BILLING SYTEM AT SUPERMARKET
total = 0

while True:
    item = input("Enter item price (or 'done' to finish): ")
    if item.lower() == "done":
        break
    price = float(item)
    total += price

print("Total Bill Amount: ₹", total)        
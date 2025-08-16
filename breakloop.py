"""Break Statement

Break ka matlab hota hai loop ko beech me tod dena.
Jab break aata hai to loop turant band ho jata hai, chahe uske baad aur iterations bachi ho.

👉 Example:"""

for i in range(1, 10):
    if i == 7:
        break    # loop yahi ruk jayega
    print(i)


#PASSWORD CHECK
password = "1234"

for attempt in range(3):   # 3 try milenge
    user = input("Enter password: ")
    if user == password:
        print("Access Granted ✅")
        break
    else:
        print("Wrong password ❌")    



#number search
numbers = [10, 20, 30, 40, 50]

for n in numbers:
    if n == 30:
        print("30 mil gaya!")
        break    # yahi par loop khatam
    print("Checking:", n)        
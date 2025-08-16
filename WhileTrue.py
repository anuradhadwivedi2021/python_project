# ye jo whiletrue loop hai infinite loop ye kbhi nhi rukta sirf break statement se hi rukhta hai
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Exiting the loop... Goodbye!")
         # Stops the loop
    
    # Convert the input to an integer and double it
    number = int(user_input)
    print(f"Double of {number} is {number * 2}")



count = 1

while True:
    print("Count:", count)
    count += 1
    
    if count > 5:  # Agar 5 se zyada ho gaya toh loop rok do
        break


while True:
    password = input("Enter password: ")
    
    if password == "1234":
        print("Access Granted ✅")
        break  # Correct password → loop stop
    else:
        print("Wrong password ❌ Try again!")



while True:
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        print(f"{num} is Even ✅")
    else:
        print(f"{num} is Odd ❌")
    
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() == "no":
        break



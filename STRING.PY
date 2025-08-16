#✅ Problem 1

#Write a program to find the length of the following string.

A = "Why fit in, When you are Born to Stand Out!"
print("Length of string is:", len(A))


"""

✅ Problem 2

Write a program to check how many times alphabet ‘o’ is occurring."""

A = "Why fit in, When you are Born to Stand Out!"
count_o = A.lower().count("o")
print("Alphabet 'o' occurs", count_o, "times")





"""✅ Problem 3

Write a program to convert the whole string into lower and upper cases."""

A = "Why fit in, When you are Born to Stand Out!"
print("Lowercase:", A.lower())
print("Uppercase:", A.upper())



"""✅ Problem 4

Write a program to convert the following string into a title."""

A = "Why fit in, When you are Born to Stand Out!"
print("Title case:", A.title())





"""✅ Problem 5

#Write a program to find the index number of “fit in"""

A = "Why fit in, When you are Born to Stand Out!"
index_val = A.find("fit in")
print("Index of 'fit in' is:", index_val)


#PATTERN
for i in range(1, 6):          # 1 se 5 rows tak
    for j in range(1, i + 1):  # har row me i numbers print karna
        print(j, end=" ")
    print()   # next line


    
#2 problem
for i in range(1,6):
    for j in range(1,6):
        print(1, end = " ")   
        print()
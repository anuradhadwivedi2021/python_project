"""🔹 Continue Statement

continue ka matlab hota hai → us iteration ko skip karo aur next iteration par chalo.
Loop band nahi hota (jaise break me hota tha), bas current wali turn ko chod deta hai.


---

✅ Example 1 – Skip even numbers"""

for i in range(1, 11):
    if i % 8 == 0:
        continue   # even numbers ko skip karega
    print(i)
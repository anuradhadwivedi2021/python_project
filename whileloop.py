#📌 Use: Jab tak condition true hai, loop chalta rahega.
i = 1
while i <= 5:
    print(i)
    i += 1   # i ko badha rahe hain, warna loop infinite ho jayega


#countdown
count = 5 
while count > 0:
    print(count)
    count -=1

    
#user se number lena jab tak 0 na de
num = int(input("Enter a number (0 to stop): "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter a number (0 to stop): "))

print("Loop ended!")        

#multiple table 
n = int(input("enter a number"))

for i in range(1,11): 
     print(n,"x" ,i, "=", n*i)


n = 0
while n >= 5:     
      n -= 1 
      print(n)
#multiply
n = 2
a = 6
while n>= 10:
      print(a,"x",i,"=",n*a)
      n+=1
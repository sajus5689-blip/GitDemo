greetings = "Good morning"
a = 5
if a>4:
    print("Condition matches")
    print("Good")
else:
    print("Condition do not matches")

print("My coding")

#for loop
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i * 2)

#range(i, j) means it will iterate num from i to j-1
for j in range(1, 6):
    print(j)

#Sum of first five natural numbers
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)
print("*************************")
#Jump 2 values for each iterations
for k in range(1, 10, 2):
    print(k)
print("**************************")
#Skipping first index
for m in range(10):
    print(m)


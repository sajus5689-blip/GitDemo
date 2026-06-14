person = ("Rahul", 25, 5.9)
print(person[1])
try:
    person[0] = "Shetty"
except Exception as e:
    print("Error:",e)
    print("Tuples cannot be modified because they are immutable.")

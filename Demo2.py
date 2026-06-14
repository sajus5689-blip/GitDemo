values = [1, 2, "rahul", 4, 5]
#List is data type that allows multiple values and can be of different datatypes

print(values[0])
print(values[2])
print(values[-1]) # -1 refers to the last index of your list
print(values[1:4]) # sublist value ie i need values 2 to 4. In this method 1:4 last index cannot be 4 it should be 4-1 thats how it works
values.insert(3, "shetty") #need to insert another string after rahul
print(values)
values.append("End") #Need to insert another string at the end of the list append is used
print(values)

values[2] = "RAHUL" #updating values in List
del values[0] #Deleting value in List
print(values)

#TUPLE - Same as LIST datatype but immutable ie not editable - Tuple uses ()
val = (1, 2, "rahul", 4.5 )
print(val[1])
#val[2] = "RAHUL" # show error because tuple is immutable
print(val[2])

#Dictionary
dic = {"a":4, 4:"bcd", "c":"Hello World"} # this is based on key not index
print(dic["a"])
print(dic[4])

#Dictionary used for excel based data
dict = {}
dict["first name"] = "rahul"
dict["last name"] = "shetty"
dict["age"] = 25
dict[5] = "New Age"
print(dict)
print(dict[5])

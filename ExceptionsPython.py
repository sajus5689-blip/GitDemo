ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2:
#    raise Exception("Products cart count not matching")
    pass

assert (ItemsInCart == 0)

# try, catch

try:
    with open("rn.txt", "r") as reader:
        reader.read()
except:
    print("File not found.")


try:
    with open("fd.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")
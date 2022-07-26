from random_strings import random_string, random_hex, random_uuid

print("PIP Example")

#Error Handling
try:
    print("RANDOM UUID: ", random_uuid(dashes=False))
except:
    print("You missed the import")

quantity = input("Enter length of your string: ")
print("RANDOM STRING: ", random_string(int(quantity)))


print("RANDOM_HEX: ", random_hex(128))



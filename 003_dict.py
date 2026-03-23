#DICT
# {}, keys, No duplicates, ordered, mutable


my_dict = {
    "Name": "Rohan",
    "Age": 35,
    "Gender": "Male",
    "Name":"Sohan"
}

# accessing dict
print(my_dict["Name"])

# keys
print(my_dict.keys())

# values
print(my_dict.values())

# key & values
print(my_dict.items())

# 
print(my_dict)

# change value
my_dict["Age"] = 25
print(my_dict)


#######################################################
# ITEMS   SYMBOL   DUPLICATES   ORDERED   MUTABLE  CALLING
# List      []          Y          Y         Y      Index
# Dict      {}          N          Y         Y      Keys
# Tuple     ()          Y          Y         N      Index
# Sets      {}          N          N         N      -
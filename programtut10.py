# Dictionary is nothing but key value pairs
d1 = {}
print(type(d1))
d2 = {"Amit":"Burger","Shruti":"Prawn","Sumit":"Roti",
      "Sonu":{"A":"maggie","B":"Roti"}}
# print(d2["Sonu"]["B"])
d2["Ankit"] = "Rice"
d2[420] = "Kebabs"
# print(d2)
# del d2[420] # to delete the keys in dict
# print(d2)

# d3 = d2
# d3 = d2.copy()
# del d2["Amit"]
# print(d3)
# print(d2["Shruti"])

# to retreieve the value of dict
# print(d2.get("Shruti"))

# To update or inset new values in dict
# print(d2.update({"Leena":"Toffee"}))
# print(d2)

print(d2.keys()) # to retreive the keys from dict
print(d2.items()) # to retreive the entire dict



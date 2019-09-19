d = {"name": "Armen", "age": 15, "grades": [10, 8, 8, 4, 6, 7] }
print(d)
d.keys()
d.values()

if "weight" in d.keys():
    print(d["weight"])
else:
    d["weight"] = input()
print(d)
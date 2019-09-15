a1=["Cookies", "Chocolate", 8, True, -3, -5, "Chocolate", 8, False, 8]
b1=[8, True, 10, 14, "Chocolate", "Milk", "Jelly", True, False, True]

set_a=set(a1)
print(set_a)
set_b=set(b1)
print(set_b)

union_ab=set_a.union(set_b)
print(union_ab)

intersection_ab=set_a.intersection(set_b)
print(intersection_ab)

union_ab.add("Kit-Kat")
union_ab.add("Oreo")
print(union_ab)

new_set=(union_ab or intersection_ab)
print(new_set)

print("Chocolate" in new_set)
new_set.remove("Oreo")
print(new_set)
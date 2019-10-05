import pretty_print as pp

def calculate_cube(x):
    return x**3

def calculate_square(x):
    return x**2

def main(a,b):
    pp.simple_print(calculate_square(a))
    pp.pro_print(calculate_cube(b))

main(3,5)
print(main(3,5))
from coche import Coche
from copy import copy

def main():
    c = Coche("azul", 4, 150, 1200)
    c2 = copy(c)
    c3 = c
    c.color = "rojo"
    print(c)
    print(c2)
    print(c3)

if __name__ == "__main__":
    main()
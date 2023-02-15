from Circle import Circle
from Rect import Rect
import math

def main():

    s1 = Rect(32, 96)
    c1 = Circle(23)
    print(s1.area())
    print(c1.get_diameter())
    print(math.pi)

if __name__ == "__main__":
    main()
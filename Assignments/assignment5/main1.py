# main.py

# Import only the needed functions from the module
from geometry import area_circle, area_rectangle

def main():
    print("Calculate Area")
    print("1. Circle")
    print("2. Rectangle")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        r = float(input("Enter radius of the circle: "))
        print(f"Area of the circle = {area_circle(r)}")
    elif choice == "2":
        l = float(input("Enter length of the rectangle: "))
        w = float(input("Enter width of the rectangle: "))
        print(f"Area of the rectangle = {area_rectangle(l, w)}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

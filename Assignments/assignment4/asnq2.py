# Lambda functions for conversions
km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda ft: ft * 12
inches_to_cm = lambda inch: inch * 2.54

# Generic converter
def distance_converter(distance, conversion_type, conversion_func):
    result = conversion_func(distance)
    print(f"{conversion_type}: {result}")

# Take a single input from user
value = float(input("Enter a distance value: "))

print("\nConverted Values:")

# Call all conversions
distance_converter(value, "Kilometers to Meters (km → m)", km_to_m)
distance_converter(value, "Meters to Centimeters (m → cm)", m_to_cm)
distance_converter(value, "Centimeters to Millimeters (cm → mm)", cm_to_mm)
distance_converter(value, "Feet to Inches (ft → in)", feet_to_inches)
distance_converter(value, "Inches to Centimeters (in → cm)", inches_to_cm)

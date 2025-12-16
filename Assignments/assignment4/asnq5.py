# Lambda functions for conversions
tonne_to_kg     = lambda t: t * 1000             
kg_to_g         = lambda kg: kg * 1000             
g_to_mg         = lambda g: g * 1000               
mg_to_lbs       = lambda mg: mg / 1_000 * 2.2046226218 / 1000  

# Ask user for input
tonnes = float(input("Enter weight in tonnes: "))

kg     = tonne_to_kg(tonnes)                       # convert to kg
grams   = kg_to_g(kg)                               # convert to g
mg      = g_to_mg(grams)                            # convert to mg
lbs     = (kg * 2.2046226218)                        # convert kg to lbs directly

# Print results
print(f"{tonnes} tonnes is:")
print(f"{kg} kilograms")
print(f"{grams} grams")
print(f"{mg} milligrams")
print(f"{lbs} pounds")

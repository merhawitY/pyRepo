fuel_level = int(input("whats the fuel level? "))

if fuel_level <= 5:
    low_fuel = True
    print("Low fuel warning: ON")
else:
    low_fuel = False

print(f" your fuel level is {fuel_level}")
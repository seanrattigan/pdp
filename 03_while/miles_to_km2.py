print("\nMiles to Km Converter")
line = "~" * 30
print(line)

while True:
    if miles >= 0:
        km = miles * 8 / 5
        print(f"{miles} miles is equal to {km}Km\n")
    else:
        print("Negative distances are not possible\n")
    repeat = input("Enter Y to go again, any other key to quit: ").lower()
    if repeat != 'y':
        break

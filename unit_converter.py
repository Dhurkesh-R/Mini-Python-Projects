def convert_length(value, from_unit, to_unit):
    conversions = {
        'm': {'km': value / 1000, 'cm': value * 100, 'mm': value * 1000},
        'km': {'m': value * 1000, 'cm': value * 100000, 'mm': value * 1000000},
        'cm': {'m': value / 100, 'km': value / 100000, 'mm': value * 10},
        'mm': {'m': value / 1000, 'km': value / 1000000, 'cm': value / 10}
    }
    return conversions.get(from_unit, {}).get(to_unit, "Invalid conversion")

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'kg': {'g': value * 1000, 'mg': value * 1000000, 'lb': value * 2.20462},
        'g': {'kg': value / 1000, 'mg': value * 1000, 'lb': value / 453.592},
        'mg': {'kg': value / 1000000, 'g': value / 1000, 'lb': value / 453592.37},
        'lb': {'kg': value / 2.20462, 'g': value * 453.592, 'mg': value * 453592.37}
    }
    return conversions.get(from_unit, {}).get(to_unit, "Invalid conversion")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'F':
            return value * 9 / 5 + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5 / 9
        elif to_unit == 'K':
            return (value + 459.67) * 5 / 9
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return value * 9 / 5 - 459.67
    return "Invalid conversion"

def main():
    while True:
        try:
            print("\nUnit Converter")
            print("Choose the type of conversion:")
            print("1. Length (m, km, cm, mm)")
            print("2. Weight (kg, g, mg, lb)")
            print("3. Temperature (C, F, K)")
            choice = input("Enter choice (1/2/3): ")

            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the from unit: ").strip()
            to_unit = input("Enter the to unit: ").strip()

            if choice == '1':
                result = convert_length(value, from_unit, to_unit)
            elif choice == '2':
                result = convert_weight(value, from_unit, to_unit)
            elif choice == '3':
                result = convert_temperature(value, from_unit, to_unit)
            else:
                result = "Invalid choice!"

            print(f"Converted value: {result}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

        again = input("Do you want to perform another conversion? (yes/no): ")
        if again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

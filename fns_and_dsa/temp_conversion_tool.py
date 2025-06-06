# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Handle User Interaction
def main():
    try:
        # Get temperature from user
        temp_input = float(input("Enter the temperature to convert: "))
        
        # Get unit from user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            converted = convert_to_celsius(temp_input)
            print(f"{temp_input}°F is {converted}°C")
            
        elif unit == "C":
            converted = convert_to_fahrenheit(temp_input)
            print(f"{temp_input}°C is {converted}°F")
            
        else:
             raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
         
    except ValueError as ve:
        print(f"Error: {ve}")
        print("Invalid temperature. Please enter a numeric value.")
        
if __name__ == "__main__":
    main()                     
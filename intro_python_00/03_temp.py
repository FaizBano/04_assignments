def fahrenheit_to_celsius():
    # Prompt the user for a temperature in Fahrenheit
    
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius using the given formula

    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0


    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

if __name__ == '__main__':
    fahrenheit_to_celsius()









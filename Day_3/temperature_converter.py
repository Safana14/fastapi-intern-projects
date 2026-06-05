def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def celsius_to_kelvin(c):
    return c + 273.15
temp = float(input("Enter temperature: "))
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
choice = input("Choose option: ")
if choice == "1":
    print(celsius_to_fahrenheit(temp))
elif choice == "2":
    print(fahrenheit_to_celsius(temp))
elif choice == "3":
    print(celsius_to_kelvin(temp))
else:
    print("Invalid choice")
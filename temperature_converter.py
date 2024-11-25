# celsius to fahrenheit convert function
def celsius_to_fahrenheit(celsius) :
  return(celsius * 9/5) + 32

# fahrenheit to celsius convert function
def fahrenheit_to_celsius(fahrenheit):
  return(fahrenheit - 32)* 5/9

# starting messages
print("Welcome to temperature converter!")
print("1: Convert Celsius to fahrenheit.")
print("2: Convert fahrenheit to celsius.")

# Get input from user
choice = input("Enter your choice (1 or 2): ")

# Calculate the temperature
# celsius to fahrenheit convert
if choice == "1":
  celsius = float(input("Enter temperature in celsius: "))
  fahrenheit = celsius_to_fahrenheit(celsius)
  print(f"{celsius}°C is equal to:  {fahrenheit: .2f}°F")

  # fahrenheit to celsius convert
elif choice == "2":
  fahrenheit = float(input("Enter temperature in fahrenheit: "))
  celsius = fahrenheit_to_celsius(fahrenheit)
  print(f"{fahrenheit}°F is equal to {celsius: .2f}°C")

else:
  print("Invalid choice! Please select 1 or 2.")


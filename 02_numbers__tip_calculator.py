# Acquire values from user and store as variables for calculation #
print("Welcome to the timp calculator!")
# get the bill total
bill_total = float(input("What was the total bill? $"))
# get the tip percentage
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15 "))
# get the number of people
number_of_people = int(input("How many people to split the bill? "))


# Calculate the bill per person
price_per_person = round((bill_total * (1 + tip_percentage / 100) / number_of_people), 2)


# Print the price per person to the user
print(f"Each person should pay: ${price_per_person:.2f}")

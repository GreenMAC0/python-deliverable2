# Step 1: The user’s name should be stored in a variable so you can use it in the Receipt.

name = input("What is your name?")

# Step 2: Display a list of fruit and their prices based on the following table: (array) (dictionary)
fruit_list = [
    ["apple",2],["grape",1],["orange",3]
    ]
fruit_totals = {
    "apple": 0,
    "grape": 0,
    "orange": 0
}

while True:
    for i in  range(len(fruit_list)):
        fruit = fruit_list [i][0]
        price = fruit_list [i][1]
        print(f"{i + 1}. {fruit.capitalize()} - ${price}")

# Step 3: Allow the user to select and buy one of the fruits from the list (prompt user for number)
    pick_fruit = int(input("Welcome " +name+ " Which fruit would you like to buy?"))
    if 1 <= pick_fruit <= len(fruit_list):
        selected_fruit = fruit_list[pick_fruit - 1][0]
        price = fruit_list[pick_fruit - 1][1]
        fruit_totals[selected_fruit] += price
            # Step 4: You will need to figure out how to track how many of each fruit has been bought.
        print(f"You bought {selected_fruit.capitalize()} at ${price}.")
     # Step 5: The user is given the option to buy another fruit or be done. This process is repeated until the user indicates they do not want to buy any more fruit.
    more_fruit = input("Do you want to buy more fruit? y/n")
    if more_fruit == "n":
            break
# Step 6: If user is done buying fruit, display a string saying "Receipt for {name}" putting their name into the string add up amount
print(f"\nReceipt for {name}:")
subtotal = 0
for fruit, total in fruit_totals.items():
    if total > 0:
        print(f"{fruit.capitalize()} - ${total}")
        subtotal += total

# Step 7: Find and print the subtotal (amount of each fruit bought * its cost all added together)
print(f"\nSubtotal: ${subtotal}")

# Step 8: Next find and print the tax (5%). Don't worry about rounding if there are extra decimals.
tax = subtotal * 0.05
print(f"Tax (5%): ${tax}")

# Step 9: Finally, add the subtotal and tax to get the receipt total. Print that. Again, don't worry about printing extra decimals.
total = subtotal + tax
print(f"Total: ${total}")

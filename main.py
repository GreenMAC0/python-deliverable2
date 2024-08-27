# Step 1: The user’s name should be stored in a variable so you can use it in the Receipt.
name = input("What is your name?")

# Step 2: Display a list of fruit and their prices based on the following table: (array) (dictionary)
fruit_list = [
    ["apple",2],["grape",1],["orange",3]
    ]
for i in  range(len(fruit_list)):
    fruit = fruit_list [i][0]
    price = fruit_list [i][1]
    print (f"{i+1}. {fruit} ${price}")

pick_fruit = int(input("Welcome" +name+ " which fruit would you like to buy?"))


# Step 3: Allow the user to select and buy one of the fruits from the list (prompt user for number)

# Step 4: You will need to figure out how to track how many of each fruit has been bought.

# Step 5: The user is given the option to buy another fruit or be done. This process is repeated until the user indicates they do not want to buy any more fruit.
#   for while loop until untrue

# Step 6: If user is done buying fruit, display a string saying "Receipt for {name}" putting their name into the string add up amount

# Step 7: Find and print the subtotal (amount of each fruit bought * its cost all added together)

# Step 8: Next find and print the tax (5%). Don't worry about rounding if there are extra decimals.

# Step 9: Finally, add the subtotal and tax to get the receipt total. Print that. Again, don't worry about printing extra decimals.
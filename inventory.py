
# Inventory Manager
# Uses a dictionary to track product names and their stock quantities.

# Read the number of commands to process.
q = int(input())

# Start with an empty inventory.
# Each dictionary key is a product name, and its value is the stock quantity.
inventory = {}

# Process exactly Q commands, one per line.
for _ in range(q):

    # Split the input into its command and arguments.
    parts = input().split()
    command = parts[0]

    # ADD: Increase stock, creating the product if it doesn't exist.
    if command == "ADD":
        name = parts[1]
        quantity = int(parts[2])

        # Default to zero when adding a new product.
        inventory[name] = inventory.get(name, 0) + quantity

    # SELL: Reduce stock only when sufficient inventory exists.
    elif command == "SELL":
        name = parts[1]
        quantity = int(parts[2])

        # Reject missing products or insufficient stock.
        # An unsuccessful sale must not change inventory.
        if inventory.get(name, 0) < quantity:
            print("ERROR")
        else:
            inventory[name] -= quantity

    # CHECK: Display current stock, or zero if the product is missing.
    elif command == "CHECK":
        name = parts[1]
        print(inventory.get(name, 0))

    # LIST: Display products with positive stock in alphabetical order.
    elif command == "LIST":

        # Filter out products with zero stock.
        available = {
            name: quantity
            for name, quantity in inventory.items()
            if quantity > 0
        }

        # Print EMPTY if no products have positive stock.
        if not available:
            print("EMPTY")
        else:
            # Sort product names alphabetically before printing.
            for name in sorted(available):
                print(name, available[name])

# Successful ADD and SELL operations produce no output.
# Input formatting is guaranteed valid by the assessment constraints.

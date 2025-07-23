# Shopping Calculator

# Get input for 3 items
price1 = float(input("Enter price of item 1: "))
quantity1 = int(input("Enter quantity of item 1: "))

price2 = float(input("Enter price of item 2: "))
quantity2 = int(input("Enter quantity of item 2: "))

price3 = float(input("Enter price of item 3: "))
quantity3 = int(input("Enter quantity of item 3: "))

# Calculate totals for each item
total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

# Calculate subtotal
subtotal = total1 + total2 + total3

# Calculate tax (8.5%)
tax = subtotal * 0.085

# Calculate final total
total = subtotal + tax

# Display results
print(f"Item 1: {price1} x {quantity1} = {total1}")
print(f"Item 2: {price2} x {quantity2} = {total2}")
print(f"Item 3: {price3} x {quantity3} = {total3}")
print(f"Subtotal: {subtotal}")
print(f"Tax (8.5%): {tax:.2f}")
print(f"Total: {total:.2f}")
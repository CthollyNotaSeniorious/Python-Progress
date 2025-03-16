# Exercise 61 - Inventory Management System
# Given a text file containing inventory data and generates a report on stock levels and restock alerts.
# This file contains columns: item_name, quantity, and price.
# Read the file and calculate the total value of the inventory.
# Identify items with stock levels below the restock threshold and store them in a list.
# Return a dictionary containing the total inventory value and the list of items that need restocking.

# Example data.txt:
# item_name,quantity,price
# Apple,100,0.5
# Banana,200,0.3
# Orange,150,0.4

# With restock threshold of 200. The function should return:
# {
#     "total_inventory_value": 170.0,
#     "restock_alerts": ["Apple", "Orange"]
# }

# The total inventory value is calculated as the sum of quantity * price for each item.
# The restock alerts are items with a quantity below the restock threshold.


def inventory_management(
    file_name: str, restock_threshold: int
) -> dict[str, list[dict[str, str]]]:
    # Your code should go here.

    ...


# cart = []

# cart.append({"item": "apples", "quantity": 4, "price_per_unit": 20},)

# print(cart)

# Start with an empty cart
# Add items: "apples", "bread", "milk", "eggs"
# Remove "bread"
# Remove the last added item
# Sort and display items alphabetically
# Display final cart with index numbers

# cart.remove('bread')

# Start with an empty cart
cart = []

# Add 10 items (as one list)
cart_items = [
    {"item": "apples", "quantity": 4, "price_per_unit": 20},
    {"item": "bread", "quantity": 2, "price_per_unit": 30},
    {"item": "milk", "quantity": 1, "price_per_unit": 45},
    {"item": "eggs", "quantity": 12, "price_per_unit": 5},
    {"item": "apples", "quantity": 6, "price_per_unit": 18},
    {"item": "bread", "quantity": 1, "price_per_unit": 28},
    {"item": "milk", "quantity": 2, "price_per_unit": 44},
    {"item": "eggs", "quantity": 6, "price_per_unit": 5},
    {"item": "cheese", "quantity": 1, "price_per_unit": 80},
    {"item": "butter", "quantity": 1, "price_per_unit": 60}
]

cart.extend(cart_items)  


def removeItemFromCart(cart,itemName):
    cart = [item for item in cart if item['item'] != itemName]  
   

removeItemFromCart(cart,"milk") 

cart.pop()  


cart.sort(key=lambda x: x['item'])

for index, item in enumerate(cart):
    print(f"{index+1}. {item['item']} - Qty: {item['quantity']}, Price: {item['price_per_unit']}")

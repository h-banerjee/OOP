class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self):
        return self.price * self.quantity

# Create an instance of Product
item1 = Product("phone", 10000, 2)

# Calculate total price for the item
item1_total_price = item1.total_price()

# Print total price
print(f"Total price for {item1.name}: {item1_total_price}")

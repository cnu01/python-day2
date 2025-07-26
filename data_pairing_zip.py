
products = ['laptop', 'tablet', 'smartphone']
prices = [10000, 5000, 30000]
quantities = [8, 20, 30]

def pair_data(products, prices, quantities):
    paired_data = []
    for product, price, quantity in zip(products, prices, quantities):
        paired_data.append((product, price, quantity))
    return paired_data

paired_data = pair_data(products, prices, quantities)
print(paired_data)



inventory_values = {product: price * quantity for product, price, quantity in paired_data}
print("Inventory values per product:", inventory_values)


product_catalog = {
    product: {"price": price, "quantity": quantity}
    for product, price, quantity in paired_data
}
print("Product Catalog:", product_catalog)

low_stock_products = [product for product, info in product_catalog.items() if info["quantity"] < 10]
print("Low stock products:", low_stock_products)
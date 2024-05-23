fruit_prices = {
    'apple': 1.0,
    'banana': 0.8,
    'orange': 1.2
}
# access the value
print(fruit_prices["banana"])

# replace the value
fruit_prices["banana"] = 6.9
print(fruit_prices["banana"])

# adding the new thing
fruit_prices["grapes"] = 1.1
print(fruit_prices)

# get all keys and values

print(fruit_prices.keys())
print(fruit_prices.values())
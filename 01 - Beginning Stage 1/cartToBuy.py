dataStore = [
    {
        "indomaret": {
            "ayam" : 30000,
            "bebek" : 30000,
            "sapi" : 100000,
            "kambing" : 200000,
            "ikan" : 20000
        },

        "alfamart": {
            "ayam" : 25000,
            "bebek" : 50000,
            "sapi" : 100000,
            "kambing" : 150000,
            "ikan" : 1000
        }
    }
]

items_to_buy = {
    "ayam" : 2,
    "bebek" : 1,
    "sapi" : 1
}

cheapest_prices = {}
for item in items_to_buy.keys():
    indomaret_price = dataStore[0]["indomaret"][item]
    alfamart_price = dataStore[0]["alfamart"][item]
    cheapest_prices[item] = min(indomaret_price, alfamart_price)

print("Harga termurah untuk setiap item:")
for item, price in cheapest_prices.items():
    print(f"{item}: {price}")

total_price = sum(cheapest_prices.values())
print(f"Total harga: {total_price}")
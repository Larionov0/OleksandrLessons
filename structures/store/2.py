store = [
    {
        'name': 'smartphone ztxcg8',
        'type': 'smartphone',
        'producer': "ZT",
        'price': 14000,
        'amount': 16
    },
    {
        'name': 'tv auogh134',
        'type': 'tv',
        'producer': "ZT",
        'price': 11400,
        'amount': 4
    },
    {
        'name': 'smart pc HD1089351',
        'type': 'pc',
        'producer': "gamerz",
        'price': 44000,
        'amount': 2
    },
    {
        'name': 'smartphone 14161tsg244',
        'type': 'smartphone',
        'producer': "gamerz",
        'price': 24500,
        'amount': 6
    },
    {
        'name': 'smart phone H',
        'type': 'smartphone',
        'producer': "ZT",
        'price': 5000,
        'amount': 76
    },
    {
        'name': 'smart pc HD1089351v2',
        'type': 'pc',
        'producer': "gamerz",
        'price': 44000,
        'amount': 4
    },
]

max_prod_names = []
max_price = 0
for product in store:
    if product['price'] > max_price:
        max_price = product['price']
        # max_prod_names = [product['name']]
        max_prod_names.clear()
        max_prod_names.append(product['name'])
    elif product['price'] == max_price:
        max_prod_names.append(product['name'])


print(max_prod_names)
print(max_price)

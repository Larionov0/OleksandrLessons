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


category_product = {
    # 'pc': ['afgararg', 13555]
}
for product in store:
    if product['type'] in category_product:
        if product['price'] < category_product[product['type']][1]:
            category_product[product['type']] = [product['name'], product['price']]
    else:
        category_product[product['type']] = [product['name'], product['price']]


print(category_product)

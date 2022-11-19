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
]


s = 0

for product in store:
    s += product['price'] * product['amount']

print(s)

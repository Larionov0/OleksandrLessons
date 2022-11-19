from pprint import pprint


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
    {
        'name': 'mega smart pc 3qgfvag43g',
        'type': 'pc',
        'producer': "gamerz",
        'price': 64000,
        'amount': 2
    },
    {
        'name': 'smart phone F',
        'type': 'smartphone',
        'producer': "ZT",
        'price': 24500,
        'amount': 23
    },
]


# find min price product + max price product + average price for every category (type)

category_products = {
    # 'pc': {
    #     'max_names': [],
    #     'max_price': 1441,
    #     'min_names': [],
    #     'min_price': 1233,
    #     'sum_price': 346535,
    #     'amount': 1
    # },
    # 'smartphone': {
    #     'max_names': [],
    #     'max_price': 1441,
    #     'min_names': [],
    #     'min_price': 1233,
    #     'sum_price': 357357,
    #     'amount': 2
    # },
}


for product in store:
    if product['type'] in category_products:
        category_parameters = category_products[product['type']]

        # max
        if product['price'] > category_parameters['max_price']:
            category_parameters['max_price'] = product['price']
            category_parameters['max_names'].clear()
            category_parameters['max_names'].append(product['name'])
        elif product['price'] == category_parameters['max_price']:
            category_parameters['max_names'].append(product['name'])

        # min
        if product['price'] < category_parameters['min_price']:
            category_parameters['min_price'] = product['price']
            category_parameters['min_names'].clear()
            category_parameters['min_names'].append(product['name'])
        elif product['price'] == category_parameters['min_price']:
            category_parameters['min_names'].append(product['name'])

        # average
        category_parameters['sum_price'] += product['price']
        category_parameters['amount'] += 1
    else:
        category_products[product['type']] = {
            'max_names': [product['name']],
            'max_price': product['price'],
            'min_names': [product['name']],
            'min_price': product['price'],
            'sum_price': product['price'],
            'amount': 1
        }


for category, category_parameters in category_products.items():
    category_parameters['average'] = category_parameters['sum_price'] / category_parameters['amount']


pprint(category_products)

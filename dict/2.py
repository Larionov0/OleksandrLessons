text = 'some text with letters and some words and some sentences'


letters_counts = {}

for letter in text:
    if letter in letters_counts:
        letters_counts[letter] += 1
    else:
        letters_counts[letter] = 1

# for k, v in letters_counts.items():
#     print(k, v)

pairs = [[k, v] for k, v in letters_counts.items()]

# print(pairs)
ogr = len(pairs) - 1
while ogr > 0:
    i = 0
    while i < ogr:
        if pairs[i][1] < pairs[i+1][1]:
            pairs[i], pairs[i+1] = pairs[i+1], pairs[i]
        i += 1
    ogr -= 1

for pair in pairs:
    print(f"{pair[0]}: {pair[1]}")

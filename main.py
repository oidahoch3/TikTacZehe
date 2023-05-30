boyfriend = {
    'name': 'Lex',
    'grades': [2, 4, 3, 1, 1, 2, 4, 3, 2, 3]
}

# Print name and average grade of boyfriend

total = sum(boyfriend['grades'])
length = len(boyfriend['grades'])

print(boyfriend['name'], total / length)

# Okay but now use a loop and not sum/len

total = 0
length = 0

for value in boyfriend['grades']:
    total = total + value
    length = length + 1

print(boyfriend['name'], total / length)

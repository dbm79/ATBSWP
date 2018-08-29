message = 'Well this is a story all about how my life flipped turned upsdie down.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
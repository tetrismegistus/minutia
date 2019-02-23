with open('input.txt', 'r') as f:
    directions = f.read()


locations = [[0, 0], [0, 0]]
visited = [[0, 0]]
driver = 0

for direction in directions:
    if direction == '>':
        locations[driver][1] += 1
    elif direction == '<':
        locations[driver][1] -= 1
    elif direction == '^':
        locations[driver][0] += 1
    elif direction == 'v':
        locations[driver][0] -= 1

    if locations[driver] not in visited:
        visited.append(locations[driver].copy())

    driver = (driver + 1) % 2

# print(visited)
print(len(visited))
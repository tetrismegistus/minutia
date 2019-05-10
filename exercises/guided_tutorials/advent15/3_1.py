with open('input.txt', 'r') as f:
    directions = f.read()

location = [0, 0]
visited = [location.copy()]


for direction in directions:
    if direction == '>':
        location[1] += 1
    elif direction == '<':
        location[1] -= 1
    elif direction == '^':
        location[0] += 1
    elif direction == 'v':
        location[0] -= 1

    if location not in visited:
        visited.append(location.copy())

print(visited)
print(len(visited))
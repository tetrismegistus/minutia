buffer = [0]
current_index = 0
stride = 348
for x in range(2017):
    current_index = ((stride + current_index) % len(buffer)) + 1
    buffer.insert(current_index, x + 1)
print(buffer[current_index + 1])

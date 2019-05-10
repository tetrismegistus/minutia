buffer = [0]
current_index = 0
stride = 348
last = 0
reps = 1
for x in range(50000000):
    if current_index == 1:
        answer = x
        print(current_index, x)
    current_index = ((stride + current_index) % (x + 1)) + 1

print(answer)


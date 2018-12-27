def seq_generator(start, factor):
    current = start
    divisor = 2147483647
    time = 40000000
    for i in range(time):
        current = (current * factor) % divisor
        yield '{:016b}'.format(current)[-16:]


gen_a = seq_generator(722, 16807)
gen_b = seq_generator(354, 48271)
matches = 0
for a, b in zip(gen_a, gen_b):
    if a == b:
        matches += 1

print(matches)

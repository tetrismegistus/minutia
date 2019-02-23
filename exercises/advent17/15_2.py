def seq_generator(start, factor, multiple):
    current = start
    divisor = 2147483647
    time = 5000000
    pair = 0
    while pair < time:
        current = (current * factor) % divisor
        if current % multiple == 0:
            pair += 1
            yield '{:016b}'.format(current)[-16:]


gen_a = seq_generator(722, 16807, 4)
gen_b = seq_generator(354, 48271, 8)
matches = 0
for a, b in zip(gen_a, gen_b):
    if a == b:
        print(a, b)
        matches += 1

print(matches)

def block_depopulator(bank):
    blocks = max(bank)
    index = bank.index(blocks)
    bank[index] = 0
    return bank, blocks, index


def socialist(bank, blocks, index):
    new_bank = bank[:]
    while blocks > 0:
        index = (index + 1) % len(bank)
        new_bank[index] += 1
        blocks -= 1
    return new_bank


def checker(bank):
    seen_configurations = []
    while True:
        seen_configurations.append(bank[:])
        bank, blocks, index = block_depopulator(bank)
        bank = socialist(bank, blocks, index)
        if bank in seen_configurations:
            return len(seen_configurations) - seen_configurations.index(bank)


def read_file(filename):
    with open(filename) as f:
        line = f.readline().strip('\n')
    line = line.split('\t')
    return [int(v) for v in line]


def main():
    bank = read_file('input.txt')
    print(bank)
    cycles = checker(bank)
    print(cycles)



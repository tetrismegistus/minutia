def read_spec(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    firewall = {}
    for line in lines:
        values = [int(i) for i in line.replace(' ', '').split(':')]
        firewall[values[0]] = values[1]
    return firewall


def check_for_hits(offset, firewall):
    for i in range(max(firewall.keys()) + 1):
        if firewall.get(i):
            if (i + offset) % (firewall[i] * 2 - 2) == 0:
                return True
    return False


def main():
    fw = read_spec('input.txt')
    time = 0
    while True:
        hit = check_for_hits(time, fw)
        if not hit:
            print('Made it at {}'.format(time))
            break
        else:
            time += 1

main()
def read_spec(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    firewall = {}
    for line in lines:
        values = [int(i) for i in line.replace(' ', '').split(':')]
        firewall[values[0]] = values[1]
    return firewall


def main():
    fw = read_spec('input.txt')
    severity = 0
    for time in range(max(fw.keys()) + 1):
        if fw.get(time):
            if time % (fw[time] * 2 - 2) == 0:
                severity += time * fw[time]
    print(severity)

main()



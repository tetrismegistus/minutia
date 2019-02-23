from hashlib import md5
key = 'yzbqklnj'
index = 0
while True:
    attempt = key + str(index)
    m = md5()
    m.update(str.encode(attempt))
    print('Attempting value of {0}. result: {1}'.format(index, m.hexdigest()))
    if m.hexdigest()[:6] == '000000':
        print('Match found!! {0} gives md5 sum of {1}'.format(index, m.hexdigest()))
        break
    index += 1


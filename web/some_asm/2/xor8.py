enc = b"xakgK\Ns9=8:9l1?im8i<89?00>88k09=nj9kimnu\00\00"
print(''.join([chr(e ^ 8) for e in enc]))

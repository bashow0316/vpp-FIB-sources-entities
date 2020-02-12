# bashow vpp fib entities
# 2020/02/12

import sys
import random

args = sys.argv

print(args)

if len(sys.argv) == 3:

    print('via    : ' +args[1]+ ' ' +args[2])

    # make entities
    entities_ipv6 = []

    # make list
    list_i = list(range(1, 256))
    list_j = list(range(1, 256))

    list_x = list(range(1, 256))
    list_y = list(range(1, 256))


    # shuffle
    random.shuffle(list_i)
    random.shuffle(list_j)

    random.shuffle(list_x)
    random.shuffle(list_y)

    for i in random.sample(list_i, 8):
        for j in random.sample(list_j, 8):
            for x in random.sample(list_x, 25):
                    for y in random.sample(list_j, 25):
                        entities_ipv6.append('ip route add 2001.0002.' +format(int(i), 'x')+format(int(j), 'x')+ '.' +format(int(x), 'x')+format(int(y), 'x')+'::/64 via ' +args[1]+ ' ' +args[2])

    # write file
    with open('vpp-ipv6-fib-entities.sh', 'w') as f:
        f.write('#!/bin/sh\n')
        f.write('\n')
        for index in entities_ipv6:
            f.write(index)
            f.write('\n')

else:
    print("No argument!")
    sys.exit()



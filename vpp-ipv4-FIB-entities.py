# bashow vpp fib entities
# 2020/02/12

import sys
import random

args = sys.argv

print(args)

if len(sys.argv) == 3:

    print('via    : ' +args[1]+ ' ' +args[2])

    # make entities
    entities_ipv4 = []

    # make list
    list_i = list(range(1, 200))
    list_j = list(range(1, 200))

    # shuffle
    random.shuffle(list_i)
    random.shuffle(list_j)

    for i in list_i:
        for j in list_j:
            # print('i : ' +str(i))
            # print('j : ' +str(j))
            entities_ipv4.append('ip route add 198.16.' +str(i)+ ',' +str(j)+ ' via ' +args[1]+ ' ' +args[2])

    # write file
    with open('vpp-ipv4-fib-entities', 'w') as f:
        for index in entities_ipv4:
            f.write(index)
            f.write('\n')

else:
    print("No argument!")
    sys.exit()




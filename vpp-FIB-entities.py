# bashow vpp fib entities
# 2020/02/12

import sys
import random



def ipv4_fib_make_script(interfaces, address):

    print('via    : ' +interfaces+ ' ' +address)

    ### make entities
    entities_ipv4 = []

    # make list
    list_i = list(range(1, 201))
    list_j = list(range(1, 201))

    # shuffle
    random.shuffle(list_i)
    random.shuffle(list_j)

    for i in list_i:
        for j in list_j:
            # print('i : ' +str(i))
            # print('j : ' +str(j))
            entities_ipv4.append(str(i)+ '.' +str(j)+ '/32 via ' +interfaces+ ' ' + address)

    ### write file
    # add entities
    with open('vpp-ipv4-add-fib-entities.sh', 'w') as f:
        f.write('#!/bin/sh\n')
        f.write('\n')
        for index in entities_ipv4:
            f.write('ip route add 198.16.' +index)
            f.write('\n')

    # del entities
    with open('vpp-ipv4-del-fib-entities.sh', 'w') as f:
        f.write('#!/bin/sh\n')
        f.write('\n')
        for index in entities_ipv4:
            f.write('ip route del 198.16.' +index)
            f.write('\n')


def ipv6_fib_make_script(interfaces, address):

    print('via    : ' +interfaces+ ' ' +address)

    ### make entities
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
                        entities_ipv6.append(format(int(i), 'x')+format(int(j), 'x')+ ':' +format(int(x), 'x')+format(int(y), 'x')+'::/64 via ' +interfaces+ ' ' +address)

    ### write file
    # add entities
    with open('vpp-ipv6-add-fib-entities.sh', 'w') as f:
        f.write('#!/bin/sh\n')
        f.write('\n')
        for index in entities_ipv6:
            f.write('ip route add 2001:0002:' +index)
            f.write('\n')

    # del entities
    with open('vpp-ipv6-del-fib-entities.sh', 'w') as f:
        f.write('#!/bin/sh\n')
        f.write('\n')
        for index in entities_ipv6:
            f.write('ip route del 2001:0002:' +index)
            f.write('\n')

if __name__ == '__main__':

    args = sys.argv
    if len(sys.argv) == 4:
        if (args[1] == 'ipv4'):
            print ('IPv4 fib entities')
            ipv4_fib_make_script(args[2], args[3])
        elif (args[1] == 'ipv6'):
            print ('IPv6 fib entities')
            ipv6_fib_make_script(args[2], args[3])
        else:
            print(ipv4 or ipv6)
            print('vpp-FIB-entities.py [ipv4/ipv6] <interfaces> <address>')
            sys.exit()

    else:
        print('No argument')
        print('vpp-FIB-entities.py [ipv4/ipv6] <interfaces> <address>')
        sys.exit()


# vpp-FIB-sources-entities
vpp-FIB-sources-entities

## ip range

```
IPv4: 198.18.0.0/15
https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
```

```
IPv6: 2001:0002::/48
https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml
```

## USE IPv4/IPv6

### IPv4: 198.16.1-200.1-200 entiries

```
python vpp-FIB-entities.py ipv4 xxx yyy
```

### make files
```
vpp-ipv4-add-fib-entities.sh
vpp-ipv4-del-fib-entities.sh
```

### output file
vpp-ipv4-add-fib-entities.sh

```
#!/bin/sh

ip route add 198.16.199.152/32 via xxx yyy
ip route add 198.16.199.57/32 via xxx yyy
ip route add 198.16.199.108/32 via xxx yyy
.
.
.
```

vpp-ipv4-del-fib-entities.sh
```
#!/bin/sh

ip route del 198.16.199.152/32 via xxx yyy
ip route del 198.16.199.57/32 via xxx yyy
ip route del 198.16.199.108/32 via xxx yyy
.
.
.
```

## IPv6: 2001:0002:ij:xy:/64 entiries

```
python vpp-FIB-entities.py ipv6 xxx yyy
```
### make file
```
vpp-ipv6-fib-add-entities.sh
vpp-ipv6-fib-del-entities.sh
```

### output file

vpp-ipv6-fib-add-entities.sh

```
#!/bin/sh

ip route add 2001:0002:4ea8:36d3::/64 via xxx yyy
ip route add 2001:0002:4ea8:36ef::/64 via xxx yyy
ip route add 2001:0002:4ea8:3689::/64 via xxx yyy
.
.
.
```

vpp-ipv6-fib-del-entities.sh

```
#!/bin/sh

ip route del 2001:0002:4ea8:36d3::/64 via xxx yyy
ip route del 2001:0002:4ea8:36ef::/64 via xxx yyy
ip route del 2001:0002:4ea8:3689::/64 via xxx yyy
.
.
.
```


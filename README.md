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

## USE IPv4 198.16.1-200.1-200 entiries

```
python vpp-ipv4-FIB-entities.py xxx yyy
```

### make files
```
vpp-ipv6-fib-entities.sh
```

### output file

```
ip route add 2001.0002.a678.4246::/64 via xxx yyy

#!/bin/sh

ip route add 198.16.9.69/32 via xxx yyy
ip route add 198.16.9.199/32 via xxx yyy
ip route add 198.16.9.54/32 via xxx yyy
.
.
.
```

## USE IPv6 IPv6: 2001:0002:ij:xy:/64 entiries

```
python vpp-ipv6-FIB-entities.py xxx yyy
```
### make file
```
vpp-ipv6-fib-entities.sh
```

### output file

```
#!/bin/sh

ip route add 2001.0002.a678.4246::/64 via xxx yyy
ip route add 2001.0002.a678.421c::/64 via xxx yyy
ip route add 2001.0002.a678.42f2::/64 via xxx yyy
.
.
.
```


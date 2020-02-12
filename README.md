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

## USE ipv4 198.16.1-200.1-200 entiries

```
python vpp-FIB-entities.py xxx yyy

```
make files
```
vpp-ipv4-fib-entities
```

output file

```
ip route add 198.16.142,107/32 via xxx yyy
.
.
.
```

## USE ipv6



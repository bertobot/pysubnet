# PySubnet

A simple python library to check if IPs or subnets are within a set of subnets.

## Example

```python

from pysubnet import Subnet

# initalize Subnet object with a list of subnets
s = Subnet(['192.168.0.0/24', '172.16.0.0/16', '10.0.0.0/8'])

# Returns True
print(s.within('192.168.0.1'))

# Returns False
print(s.within('192.168.1.1'))

# Returns True
print(s.within('172.16.17.25'))

# Returns False
print(s.within('11.11.11.11'))

# Returns True
print(s.within('10.11.11.11'))


# convenience methods

# add a single subnet to the master list
s.add_subnet('192.168.1.0/25')

# add a list 
s.add_subnets(['192.168.2.0/24', '192.168.3.0/24'])
```

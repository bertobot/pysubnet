# 
# MIT License
# 
# Copyright (c) 2018 Fairfax Smartware
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

import re

class Subnet(object):
    def __init__(self, subnets):
        self.subnets = []
        if isinstance(subnets, list):
            self.subnets = subnets

    def add_subnet(self, subnet):
        self.subnets.append(subnet)

    def add_subnets(self, subnets):
        self.subnets = self.subnets + subnets

    def within(self, subnet):
        """ returns true if subnet part of subnets """

        ip = subnet
        cidr = 32

        m = re.search(r'(.+?)/(\d+)', subnet)

        if m:
            ip = m.group(1)
            cidr = int(m.group(2))

        for s in self.subnets:
            sic = s.split('/')
            sic[1] = int(sic[1])

            sn = self._subnet_to_bin(sic[0], sic[1])
            si = self._subnet_to_bin(ip, sic[1])

            if si == sn:
                return True

        return False

    def _subnet_to_bin(self, ip, cidr=32):
        mBin = 0

        for o in ip.split('.'):
            mBin = mBin << 8
            mBin = mBin | (int(o) & 0xff)

        mask = ''
        count = 0
        for i in range(0, 32):
            if count < cidr:
                mask = mask + '1'
            else:
                mask = mask + '0'
            count = count + 1

        mask = int(mask, 2)
        return mBin & mask
        

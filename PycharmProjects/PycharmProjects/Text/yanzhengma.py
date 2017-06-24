#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/6/23 下午8:18
# @Author  : Panda
import random
stochastic=''

for shu in range(4):
    caishu=random.randint(0,5)
    if shu==caishu:
        tem=chr(random.randint(65,90))
    else:
        tem=random.randint(0,9)

    stochastic+=str(tem)

print(stochastic)
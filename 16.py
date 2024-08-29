# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:53:12 2024

@author: Admin
"""

h=int(input("nhập h"))
p=int(input("nhập p"))
s=int(input("nhập s"))
hps= "{}h/{}p/{}s".format(h,p,s)
print(hps)
tong= h*3600 + p*60 + s
print("Tổng giây", tong)
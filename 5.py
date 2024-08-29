# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:40:50 2024

@author: Admin
"""


h=int(input("nhập giờ:"))
m=int(input("nhập phút"))
s=int(input("nhập giây"))
hps="{}h:{}m:{}s".format(h,m,s)
print(hps)
doi_s= (h*3600)+(m*60)+s
print("Tổng giây", doi_s)
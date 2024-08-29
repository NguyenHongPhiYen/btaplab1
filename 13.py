# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:52:04 2024

@author: Admin
"""

a=int(input("nhập ngày sinh:"))
b=int(input("nhập tháng sinh:"))
c=int(input("nhập năm sinh:"))
# Trường hợp a: In ngày/tháng/năm
cau_a = "{}/{}/{}".format(a, b, c)
print(cau_a)

# Trường hợp b: In ngày/tháng/2 chữ số cuối của năm
cau_b = "{}/{}/{}".format(a, b, c % 100)
print(cau_b)

# Trường hợp c: In năm/tháng/ngày
cau_c = "{}/{}/{}".format(c, b, a)
print(cau_c)
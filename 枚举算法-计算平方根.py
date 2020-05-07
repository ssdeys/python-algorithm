#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

x = 25
epsilon = 0.01
step = epsilon**2 #幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
numGuesses = 0
ans = 0.03
high= 6.25
ans= 4.6875
low= 4.6875

while abs(ans**2 - x) >= epsilon and ans <= x:#and关键字 和 
    #abs() 函数返回数字的绝对值。
    ans += step
    numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)
    
'''
枚举算法的一种，没有导入库，基础的运算，相对比较简单，注意运算优先级

'''


#!/usr/bin/env python
# coding: utf-8

# # 24点游戏

# In[25]:


import itertools
#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数

#官方文档https://docs.python.org/2/library/itertools.html

def twentyfour(cards):#定义函数，不懂的需要复习了
    '''
    史上最短计算24点代码
    4个数，使用+-*/达到结果等于24
    
    '''
    
    for nums in itertools.permutations(cards): # 四个数，
        
        '''
        itertools.permutations() 通俗地讲，就是返回可迭代对象的所有数学全排列方式。
        简单举例：
        >>> for i in itertools.permutations('123', 2):
             print i

  输出结果      ('1', '2')
                ('1', '3')
                ('2', '1')
                ('2', '3')
                ('3', '1')
                ('3', '2')
        实际中num的结果 
        
        print("nums is ",nums)
        nums is  (1, 1, 1, 8)
        nums is  (1, 1, 8, 1)
        nums is  (1, 1, 1, 8)
        ......
        None
        '''
        

        for ops in itertools.product('+-*/', repeat=3):  # 三个运算符（可重复！）
        
#         itertools.product 用于求多个可迭代对象的笛卡尔积(Cartesian Product)，它跟嵌套的 for 循环等价.即:
#         product(A, B) 和 ((x,y) for x in A for y in B)一样.
#         repeat=3  三个运算符（可重复！） +++ --- *** /// +-/等等，因为是4个数字，所以要3个运算符号


            # 构造三种中缀表达式 (bsd)
            bds1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)  # (a+b)*(c-d)
            #这里格式化是按照顺序取值，0123，取*nums，456取*ops 可以单独跑以下代码
            '''
            import itertools

            nums=(1,1,1,8)
            for ops in itertools.product('+-*/', repeat=3):
                bds1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)  # (a+b)*(c-d)
                print(bds1)#自己更换数字位置，就看明白了
            
            '''
            bds2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)  # (a+b)*c-d
            bds3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)  # a/(b-(c/d))

            for bds in [bds1, bds2, bds3]:  # 遍历
                try:#捕获异常
                    if abs(eval(bds) - 24.0) < 1e-10:  # eval函数   1e-10 1乘10的-10次方 int(1e-10)为0 
                        #1e-10 为什么要用1e-10，其实目的是0，1e-1000都行，如果直接写0，如果eval(bds) - 24.0除数=0，下面异常，为了除数不能为0
                        #abs() 函数返回数字的绝对值。eval() 函数用来执行一个字符串表达式，并返回表达式的值。
                        return bds
                except ZeroDivisionError:  # 零除错误！
                    continue

    return 'Not found!'#找完结束


# 测试
cards = [[1, 1, 1, 8],
         [1, 1, 2, 6],
         [1, 1, 2, 7],
         [1, 1, 2, 8],
         [1, 1, 2, 9],
         [1, 1, 2, 10],
         [1, 1, 3, 4],
         [1, 1, 3, 5],
         [1, 1, 3, 6],]
        

for card in cards:
    print(twentyfour(card))
# 新知识 itertools abs eval 1e-10 format(*nums,...)




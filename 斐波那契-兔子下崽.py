fib_table = {}  # memoization table to store previous terms

def fib_num(n):

    if (n <= 1):#输入n值是否<=1 
        return n#如果<=1返回n
    if n not in fib_table:
        fib_table[n] = fib_num(n - 1) + fib_num(n - 2)
        #这个是最终是指向列表中的value，计算fib_table[n-1]+fib_table[n-2]的value的值
        
        print("第{}次 ".format(n), fib_table[n],fib_table)
    return fib_table[n]

n = int(input("输入斐波那契数列的第n项 \n"))
print("斐波那契数数列的第 ", n, "项是",fib_num(n))

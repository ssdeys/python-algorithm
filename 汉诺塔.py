#双重调用，不是很懂多思考吧，下次明白了再补充
i = 1
def move(n, mfrom, mto) :
  global i  
  print("第{}次,n是{},{},{}".format(i,n,mfrom,mto))  
  
  # Python中定义函数时，若想在函数内部对函数外的变量进行操作，就需要在函数内部声明其为global。
  # 这里定义global i 为了内部能调用修改
  print("第%d步:将%d号盘子从%s -> %s" %(i, n, mfrom, mto))
  i += 1

def hanoi(n, A, B, C) :
  if n == 1 :
    move(1, A, C)
  else :
    hanoi(n - 1, A, C, B)
    
    move(n, A, C)
    
    
    hanoi(n - 1, B, A, C)
    
#********************程序入口**********************
try :
  n = int(input("please input a integer :"))
  print("移动步骤如下：")
  hanoi(n, 'A', 'B', 'C')
except ValueError:
  print("please input a integer n(n > 0)!" )

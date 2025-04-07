"""
打印杨辉三角

题目:
找出规律，并根据输入m(1≤m≤100)总行数，输出对应的数字图形(先生成再输出，每个数据所占场宽为4)。

输入 一行，包含一个整数m。 输出 m行，表示杨辉三角，具体见样例

样例输入：4

样例输出：
1 

1 1

1 2 1

1 2 3 1
"""
lastlist = {}
num = input()
for i in range(num):
  if i == 0:
    print(1)
    lastlist = [1,]
  for j in range (i+1):
      if i == 0 or :
        print("1 ")
      elif i + 1 == j:
        print("1")
      else:
        print(str (lastlist[i-1] +lastlist[i]) +" ")
  print("\n")
     
      

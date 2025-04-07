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

1 3 3 1
"""
lastlist = {}
num = int(input())
for i in range(num):
  if i == 0:
    print(1,end="")
    lastlist =  {0:1,}
  else:
    nowlist = {}
    for j in range (i+1):
        if j == 0  :
            r = 1
            print("1 ",end="")
        elif i == j:
            r = 1
            print("1",end="")
        else:
            r = lastlist[j-1] +lastlist[j]
            print(str (r) +" ",end="")
        nowlist[j] = r 
    lastlist = nowlist
  print("\n")

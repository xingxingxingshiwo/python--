# 打印出来一个心的形状
import time
sentence = "521" # 换成女神的名字也挺好
for char in sentence.split():
   allChar = []
   for y in range(12, -12, -1):
       lst = []
       lst_con = ''
       for x in range(-30, 30):
            formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
       lst.append(lst_con)
       allChar += lst
   print('\033[0;32m'+'\n'.join(allChar)+'\033[0m')   # 设置字体颜色和背景
   time.sleep(1)
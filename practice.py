import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('test1112012.csv')#csvからデータを抽出
#array



data2 = data[0:100]#50行目から150行目までを抽出
lst = data2.values.tolist()#csvデータを配列にする
c1 = data2['0']#1列目を指定して抽出,額の温度
c1 = pd.DataFrame(c1)#データの番号が50~79までなので、0~に直す
#lst2 = c1.values.tolist()#csvデータを配列にする
#print(lst2)
print(data2)
b = np.array(c1)
print(b)
#a = np.array([0.0,1.0,2.0,3.0,4.0,5.0,6.0])

#print(a)
#c2 = data2['0.1']#2列目を指定して抽出,鼻の温度
#c2 = pd.DataFrame(c2)#データの番号が50~79までなので、0~に直す

#x = np.linspace(0, 10, 500)

print(c1)
#print(data2)
#print(c2)

n = 3#移動平均の点数
ave1 = np.convolve(c1, np.ones(n)/float(n), 'valid')#移動平均の計算

#v = np.ones(3)/3.0
#ave1 = np.convolve(a, v, 'same')
#print(ave1)

#ave2 = np.convolve(c2, np.ones(n)/float(n), 'valid')
#print(ave2)

#plt.plot(c1, 'r', linewidth = 1)
plt.plot(ave1, 'b', linewidth = 1)
plt.show()
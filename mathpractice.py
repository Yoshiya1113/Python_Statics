import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('csvtest.csv')
rx = data[['a']]
ry = data[['b']]
lx = data[['e']]
ly = data[['f']]

print(data)
plt.scatter(rx, ry, s=600, c="pink", alpha=0.5, linewidths="2",
            edgecolors="red")
plt.scatter(lx, ly, s=600, c="lightblue",marker="*", alpha=0.5, linewidths="2",
            edgecolors="blue")
plt.show()
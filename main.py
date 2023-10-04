import pandas as pd
import matplotlib.pyplot as plt

path = './data/values.csv'
df = pd.read_csv(path)

data = df.values
x, y = data[:, 0], data[:, 1]

calculo = x * 2

plt.figure()
plt.plot(x, y, linewidth=13 )
plt.savefig('grafico_A.png')

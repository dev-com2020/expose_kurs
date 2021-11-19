import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
print(df)
x = df['date']
y = df['Close']

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y)

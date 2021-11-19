import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
print(df)
x = df['date']
y = df['Close']

# df.plot(x='date', y='Close', legend=False) # w pandasie

#plt.style.use('ggplot')
# plt.style.use('seaborn-poster')
fig, ax = plt.subplots(2,2,figsize=(10, 8))
ax[1,1].pie([10,5], labels=['10','5'])
ax[1,0].bar(x, y)
ax[0,1].scatter(x, y)
ax[0,0].plot(x, y)
#line = res[0]
# line.set_c('red')
# line.set_linestyle('dashed')
# title = ax.set_title('Kurs dolara')
# title.set_position((.2, .7))
# yax = ax.get_yaxis()
# yax.set_ticks([-50, 500, 5000, 20000, 30000])
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.text(ax.get_xlim()[0], 5000, 'Dolar', clip_on=True, family='Times New Roman', size=20)
# ax.text(ax.get_xlim()[0], 10000, 'Inny tekst', clip_on=True, family='Serif', size=20, style='italic',
#         bbox={'facecolor': 'red', 'alpha': .5})
#
# print(plt.style.available)
plt.show()

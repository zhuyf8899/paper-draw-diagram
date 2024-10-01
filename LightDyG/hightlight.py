import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools

models = ["ROLAND", "LightDyG"]
bar_data = {
    "Model": [val for val in models for i in range(5)] ,
    "Dataset": ["BTC-Alpha", "BTC-OTC", "DBLP", "Reddit-title", "UCI"]*2,
    "Parameter Size":[
        356,     356,     420,     440,     356, # ROLAND
        220,     56,      188,     252,     104 #LightDyG
    ],
}
print(len(bar_data['Model']))
print(len(bar_data['Dataset']))
print(len(bar_data['Parameter Size']))

ylabel_font_size = 12
legend_font_size =12

df= pd.DataFrame(bar_data)
#sns.set_color_codes("muted")
plt.rc('font',family='Arial')

fig = plt.figure(num=1, figsize=(10,8))
ax1 = fig.add_subplot(211)

bar_width=0.4
x=np.arange(5)
size_roland=[356,     356,     420,     440,     356]
size_LDG=[220,     56,      188,     252,     104]
tick_label=["Bitcoin-Alpha", "Bitcoin-OTC", "DBLP", "Reddit-title", "UCI"]
ax1.bar(x, size_roland, bar_width, align="center", color="#4878AE", label="ROLAND", alpha=1)
ax1.bar(x+bar_width, size_LDG, bar_width, color="#DB7624", label="LightDyG",alpha=1)
plt.xticks(x+bar_width/2, tick_label)
# ax1 = sns.barplot(y = 'Dataset',
#             x = 'Parameter Size',
#             hue = 'Model',
#             data = df,
#             orient='h'
#             )

ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18), ncol=3, fancybox=True, fontsize=legend_font_size)
ax1.set_ylabel(u"", fontsize=ylabel_font_size) #Y轴标签
ax1.set_xlabel(u"Parameter size", fontsize=ylabel_font_size+4) #X轴标签
ax1.tick_params(labelsize=ylabel_font_size)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
#ax1.spines['bottom'].set_visible(False)
#ax.spines['left'].set_visible(False)

ax2 = fig.add_subplot(212)
# BTC-A, BTC-O, DBLP, Reddit, UCI
x=np.arange(5)
mrr_roland=[14.52, 16.54, 6.6, 35.11, 11.84]
mrr_LDG=[36.74, 37.94, 7.46, 29.91, 21.69]
std_roland=[0.6506, 1.2191, 0.0047, 0.0928, 0.2561]
std_LDG=[3.9389, 1.7019, 0.0020, 0.0829, 0.3383]
error_attri={"elinewidth":2,"ecolor":"black","capsize":4}
bar_width=0.4
tick_label=["BTC-Alpha", "BTC-OTC", "DBLP", "Reddit-title", "UCI"]
#创建图形，
ax2.bar( x, mrr_roland, bar_width, align="center", color="#4878AE", yerr=std_roland, error_kw=error_attri, label="ROLAND", alpha=1)
ax2.bar( x+bar_width, mrr_LDG, bar_width, yerr=std_LDG, color="#DB7624", error_kw=error_attri, label="LightDyG",alpha=1)
#创建辅助标签
ax2.set_ylabel(u"", fontsize=ylabel_font_size) #Y轴标签
ax2.set_xlabel(u"MRR performance", fontsize=ylabel_font_size+4) #X轴标签
plt.xticks(x+bar_width/2,tick_label)
ax2.tick_params(labelsize=ylabel_font_size)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("highlight.png")
plt.show()
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools

models = ["EvloveGCN-H", "EvloveGCN-O", "DGNN",  "dyngraph2vec", "ROLAND", "WinGNN"]
bar_data = {
    "Model": [val for val in models for i in range(6)] ,
    "Dataset": ["Bitcoin-Alpha", "Bitcoin-OTC", "DBLP", "Reddit-title", "Stack Overflow", "UCI"]*6,
    "Parameter Size":[
        2650000,    228000,     1100000,    2650000,    228000,       228000, # EvloveGCN-H
        2650000,    228000,     1100000,    2650000,    228000,       228000, # EvloveGCN-O
        12000000,   2200000,    12000000,   11000000,   2200000,      2200000, # DGNN
        31000000,   3100000,    3100000,    31000000,   31000000,     3100000, # dyngraph2vec
        356000,     356000,     420000,     440000,     356000,       356000, # ROLAND
        220000,     56000,      188000,     252000,     220000,       104000 #WinGNN

    ],
}
print(len(bar_data['Model']))
print(len(bar_data['Dataset']))
print(len(bar_data['Parameter Size']))

ylabel_font_size = 16
plt.rc('font',family='Times New Roman')
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

df= pd.DataFrame(bar_data)

colors = ["darkgreen", "firebrick", "moccasin", "forestgreen", "c", "royalblue"]

ax = sns.barplot(x = 'Dataset',
            y = 'Parameter Size',
            hue = 'Model',
            data = df, palette=sns.color_palette("Blues"))

num_locations = len(models)
# hatches = itertools.cycle(['//', '+', '-', 'x', '*', 'o', 'O', '.','/','\\'])
# for i, bar in enumerate(ax.patches):
#     if i == 0 or bar_data['Model'][i-1] != bar_data['Model'][i]:
#         hatch = next(hatches)
#     bar.set_hatch(hatch)

ax.set_ylim((0, 3e6))
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol=3, fancybox=True)
ax.set_ylabel(u"Parameter size", fontsize=ylabel_font_size) #Y轴标签
ax.set_xlabel(u"Datasets", fontsize=ylabel_font_size) #X轴标签


# Show the plot
plt.tight_layout()
plt.savefig("para_size.png")
plt.show()
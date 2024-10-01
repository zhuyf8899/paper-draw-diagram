import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools

#sns.set_color_codes("muted")
plt.rc('font',family='Times New Roman')

fig = plt.figure(num=1, figsize=(10,5))
ax1 = fig.add_subplot(111)


legend_font_size = 14
ylabel_font_size = 16
bar_width=0.2
error_attri={"elinewidth":2,"ecolor":"black","capsize":4}
x=np.arange(2)
mrr_EvolveGCN_H=[3.28,    8.17]
err_EvolveGCN_H=[0.2845, 0.2284]
mrr_EvolveGCN_O=[2.52,    10.81]
err_EvolveGCN_O=[0.1014, 0.5327]
mrr_ROLAND=[14.52,    11.84]
err_ROLAND=[0.6506, 0.2501]
mrr_WinGNN=[36.74,    21.69]
err_WinGNN=[3.9389, 0.3383]
tick_label=["Bitcoin-Alpha", "UCI"]
ax1.bar( x, mrr_EvolveGCN_H, bar_width, align="center", color="#ACD6FF", yerr=err_EvolveGCN_H, error_kw=error_attri, label="EvolveGCN-H", alpha=1)
ax1.bar( x+bar_width, mrr_EvolveGCN_O, bar_width, yerr=err_EvolveGCN_O, color="#66B3FF", error_kw=error_attri, label="EvolveGCN-O",alpha=1)
ax1.bar( x+2*bar_width, mrr_ROLAND, bar_width, yerr=err_ROLAND, color="#0072E3", error_kw=error_attri, label="ROLAND",alpha=1)
ax1.bar( x+3*bar_width, mrr_WinGNN, bar_width, yerr=err_WinGNN, color="#003D79", error_kw=error_attri, label="WinGNN",alpha=1)
plt.xticks(x+bar_width*1.5, tick_label)
# ax1 = sns.barplot(y = 'Dataset',
#             x = 'Parameter Size',
#             hue = 'Model',
#             data = df,
#             orient='h'
#             )

ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18), ncol=4, fancybox=True, fontsize=legend_font_size)
ax1.set_ylabel(u"", fontsize=ylabel_font_size) #Y轴标签
ax1.set_xlabel(u"", fontsize=ylabel_font_size+4) #X轴标签
ax1.tick_params(labelsize=ylabel_font_size)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
#ax1.spines['bottom'].set_visible(False)
#ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig("highlight.png")
plt.show()
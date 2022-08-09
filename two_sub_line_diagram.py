#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os

dims = [1, 2, 3, 4, 5,6 ,7 ]
dims_name = [
    r"$8$",
    r"$16$",
    r"$32$",
    r"$64$",
    r"$128$",
    r"$256$",
    r"$512$",
    ]
# dims_name = [
#     r"$0$",
#     r"$-2$",
#     r"$-3$",
#     r"$-4$",
#     r"$-5$",
#     r"$-6$"
#     ]

legend_font_size = 45
margins = 0.15
ylabel_font_size = 66
title_font_size = 68
y_trick_font_size = 50
x_trick_font_size = 50
ms_size = 38

# x = range(len(dims))
x = dims
fig = plt.figure(num=1, figsize=(36, 12))
ax1 = fig.add_subplot(121)

y_f1 = [0.5149, 0.5178, 0.5221, 0.5168, 0.5109, 0.5131, 0.5078]
y_precision = [0.5988, 0.5642, 0.6340, 0.5609, 0.5551, 0.5355, 0.5296]
y_recall = [0.4516, 0.4784,0.4438, 0.4791, 0.4732, 0.4925, 0.4877]
y_comm_size = [2029, 2281, 1883, 2298, 2293, 2474, 2477]

ax1.plot(x, y_f1, marker='o', ms=ms_size, mec='black', mew=2, label=r'F1', linewidth=7)
ax1.plot(x, y_precision, marker='d', ms=ms_size, mec='black', mew=2, label=r'Precision', linewidth=7)
ax1.plot(x, y_recall, marker='v', ms=ms_size, mec='black', mew=2, label=r'Recall', linewidth=7)
ax1.legend(fontsize=legend_font_size, loc="upper right")  # 让图例生效
plt.xticks(dims, fontsize=x_trick_font_size)
ax1.set_xticklabels(dims_name)
# ax1.tick_params(labelsize=x_trick_font_size)
# ax1.set_xticklabels(['12', "13", "21", '23', '31', '32'])
# ax1.set_xticks([64, 128, 256, 512])
ax1.margins(margins)
# ax1.subplots_adjust(bottom=0.15)
ax1.set_xlabel(u"Embedding Size", fontsize=ylabel_font_size) #X轴标签
# ax1.set_ylim((0.17, 0.25))
# y_tick11 = np.linspace(0.17, 0.27, 4)
# plt.yticks(y_tick11, fontsize=y_trick_font_size)
ax1.set_ylabel("Scores", fontsize=ylabel_font_size) #Y轴标签
ax1.set_title("", fontsize=title_font_size) #标题
# ax1.savefig("emb-gowalla-recall.pdf")
# plt.show()
ax1.tick_params(labelsize=y_trick_font_size, direction='in', length=20, width=5)
ax1.set_ylim((0.35, 0.65))
ax1.set_yticks(np.arange(0.35, 0.66, 0.1))
ax1.grid()

# ax12 = ax1.twinx()
# ax12.plot(x, y_comm_size, marker='*', ms=ms_size,mec='black', mew=2, label=r'$Yelp2018$', color='red', linewidth=7)
# ax12.set_ylabel("Community size", fontsize=ylabel_font_size) #Y轴标签
# # ax12.tick_params(labelsize=x_trick_font_size)
# # plt.xticks(dims, fontsize=20)
# # plt.yticks(fontsize=20)
# # ax12.set_ylim((0.0415, 0.0423))
# # y_tick12 = np.linspace(0.0416, 0.0426, 4)
# plt.xticks(dims, fontsize=x_trick_font_size)
# # plt.yticks(y_tick12, fontsize=y_trick_font_size)
# ax12.tick_params(labelsize=y_trick_font_size, direction='in', length=20, width=5)
# ax12.set_ylim((0.063, 0.067))
# ax12.set_yticks(np.arange(0.063, 0.067, 0.0012))
# ax12.legend(fontsize=legend_font_size, loc="upper right")  # 让图例生效

# fig.legend(fontsize=legend_font_size, bbox_to_anchor=(1,1), loc="upper right", bbox_transform=ax1.transAxes)
# plt.savefig("L2-recall.pdf")
# plt.show()


ax2 = fig.add_subplot(122)
# AMiner = [0.0979, 0.0864, 0.0940, 0.0985, 0.0963, 0.0979]

#ax2.plot(x, y_comm_size, marker='o', ms=ms_size,mec='black', mew=2, label=r'Community size', linewidth=7)
bars1 = ax2.bar(x, y_comm_size, width=0.6, align='center', alpha=0.8, tick_label=dims_name)
#给每个柱子上面添加标注
# for b in bars1: #遍历每个柱子
#     height = b.get_height()
#     ax2.annotate('{}'.format(height),
#         #xy控制的是，标注哪个点，x=x坐标+width/2, y=height，即柱子上平面的中间
#         xy=(b.get_x() + b.get_width() / 2, height), 
#         xytext=(0,3), #文本放置的位置，如果有textcoords，则表示是针对xy位置的偏移，否则是图中的固定位置
#         textcoords="offset points", #两个选项 'offset pixels'，'offset pixels'
#         va = 'bottom', ha = 'center' #代表verticalalignment 和horizontalalignment，控制水平对齐和垂直对齐。
#         )
# ax2.legend(fontsize=legend_font_size, loc="upper left")  # 让图例生效
# ax2.set_xticks(x, dims, fontsize=14)
ax2.set_xticks(dims)
ax2.set_xticklabels(dims_name, weight='bold')
#ax2.tick_params(labelsize=x_trick_font_size, direction='in', length=20, width=5)
plt.xticks(dims, fontsize=x_trick_font_size)
plt.yticks(fontsize=y_trick_font_size)
# ax2.set_xticklabels(['12', "13", "21", '23', '31', '32'])
ax2.margins(margins)
# ax2.subplots_adjust(bottom=0.15)
ax2.set_xlabel(u"Embedding Size", fontsize=ylabel_font_size) #X轴标签
# ax2.set_ylabel("Recall", fontsize=15) #Y轴标签
# ax2.set_ylim((0.08, 0.105))
# y_tick = np.linspace(0.075, 0.11, 4)
ax2.set_ylabel("Community Size", fontsize=ylabel_font_size) #Y轴标签
ax2.set_title("", fontsize=title_font_size) #标题
# ax2.savefig("emb-gowalla-ndcg.pdf")
# plt.show()
# ax2.tick_params(labelsize=y_trick_font_size)
ax2.tick_params(labelsize=y_trick_font_size, direction='in', length=20, width=5)
ax2.set_ylim((1000, 3000))
ax2.set_yticks(np.arange(1000, 3001, 500))
ax2.grid()

# ax22 = ax2.twinx()
# ax22.plot(x, Yelp2018, marker='*', ms=ms_size,mec='black', mew=2, label=r'$Yelp2018$', color='red', linewidth=7)
# # ax22.set_ylim((0.0185, 0.0194))
# y_tick = np.linspace(0.0185, 0.0194, 4)
# ax22.tick_params(labelsize=x_trick_font_size)
# ax22.set_ylabel("NDCG(Yelp2018)", fontsize=ylabel_font_size,rotation=90) #Y轴标签
# plt.xticks(dims, fontsize=y_trick_font_size)
# plt.yticks(fontsize=y_trick_font_size)
# ax22.tick_params(labelsize=y_trick_font_size, direction='in', length=20, width=5)
# ax22.set_ylim((0.0515, 0.0552))
# ax22.set_yticks(np.arange(0.0515, 0.0552, 0.0012))

# ax22.legend(fontsize=legend_font_size,  loc="upper right")  # 让图例生效

# lines, labels = fig.axes[-1].get_legend_handles_labels()
# fig.legend(lines, labels, fontsize=legend_font_size,  bbox_to_anchor=(1.01, 0.1), ncol=2, loc='center')  ##设置ax4中legend的位置，将其放在图外
# fig.legend(fontsize=legend_font_size, bbox_to_anchor=(1,1), loc="upper right", bbox_transform=ax1.transAxes)
# ax2.legend(fontsize=legend_font_size, bbox_to_anchor=(1,1), loc="upper left", bbox_transform=ax2.transAxes)
# ax22.legend(fontsize=legend_font_size, bbox_to_anchor=(1,1), loc="upper right", bbox_transform=ax22.transAxes)

# plt.subplots_adjust(left=0.1, bottom=0.1, right=1, top=1, wspace=0.15, hspace=0.15)
# fig.legend(fontsize=legend_font_size, bbox_to_anchor=(1,1), loc="upper right", bbox_transform=ax2.transAxes)
# fig.legend(loc = (0.5, 0), ncol=1)
plt.tight_layout()
plt.savefig("emb_size.pdf")
#plt.show()
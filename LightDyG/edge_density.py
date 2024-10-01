#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os

fn_btc_alpha = 'LightDyG/bitcoinalpha-density.npy'
fn_btc_otc = 'LightDyG/bitcoinotc-density.npy'
fn_dblp = 'LightDyG/dblp_density.npy'
fn_reddit = 'LightDyG/reddit_title_density.npy'
fn_stack = 'LightDyG/stackoverflow_density.npy'
fn_uci = 'LightDyG/uci-msg-density.npy'

#settings 
legend_font_size = 18
margins = 0.15
ylabel_font_size = 18
title_font_size = 24
y_trick_font_size = 20
x_trick_font_size = 20
ms_size = 8


btc_alpha = np.load(fn_btc_alpha) / 3783**2
btc_otc = np.load(fn_btc_otc) / 5881**2
dblp = np.load(fn_dblp) / 28086**2
reddit = np.load(fn_reddit) / 54075**2
uci = np.load(fn_uci) / 1899**2
stack = np.load(fn_stack) / 1601977**2

data = [btc_alpha, btc_otc, dblp, reddit, stack, uci]
for each_data in data:
    print("This set has {} snapshots, avg. density is: {}".format(len(each_data), np.mean(each_data)))

plt.rc('font',family='Times New Roman')

fig = plt.figure(num=1, figsize=(14, 6))
ax0 = fig.add_subplot(131)
ax0.ticklabel_format(style='sci', scilimits=(0,0), axis='y')

ax0.plot([-1], [-1], mew=1, label=u'Bitcoin-Alpha', linewidth=3)
ax0.plot([-1], [-1],  mew=1, label=u'Bitcoin-OTC', linewidth=3)
ax0.plot([-1], [-1], mew=1, label=u'DBLP', linewidth=3)
ax0.plot([i for i in range(1,len(reddit)+1)], reddit, mew=1, label=u'Reddit-title', linewidth=3)
ax0.plot([i for i in range(1,len(stack)+1)], stack, mew=1, label=u'Stack Overflow', linewidth=3)
ax0.plot([-1], [-1], mew=1, label=u'UCI', linewidth=3)

ax0.margins(margins)
ax0.set_xlabel(u"Snapshots", fontsize=ylabel_font_size) #X轴标签
ax0.set_xlim((0, 180))
# plt.yticks(y_tick11, fontsize=y_trick_font_size)
ax0.set_ylabel("Density", fontsize=ylabel_font_size) #Y轴标签
ax0.set_title("", fontsize=title_font_size) #标题
ax0.tick_params(labelsize=y_trick_font_size, direction='in', length=5, width=1)

ax0.set_ylim((1e-6, 2.5e-5))
#ax1.set_yticks(np.arange(0.35, 0.66, 0.1))
ax0.grid()


ax1 = fig.add_subplot(132)
ax1.ticklabel_format(style='sci', scilimits=(0,0), axis='y')


ax1.plot([-1], [-1], mew=1, label=u'Bitcoin-Alpha', linewidth=3)
ax1.plot([i for i in range(1,len(btc_otc)+1)], btc_otc, mew=1, label=u'Bitcoin-OTC', linewidth=3)
ax1.plot([i for i in range(1,len(dblp)+1)], dblp, mew=1, label=u'DBLP', linewidth=3)
ax1.plot([-1], [-1], mew=1, label=u'Reddit-title', linewidth=3)
ax1.plot([-1], [-1], mew=1, label=u'Stack Overflow', linewidth=3)
ax1.plot([-1], [-1], mew=1, label=u'UCI', linewidth=3)

# ax1.plot([i for i in range(1,len(btc_alpha)+1)], btc_alpha, marker='o', ms=ms_size, mec='black', mew=1, label=r'Bitcoin-Alpha', linewidth=2, linestyle='dashed')
# ax1.plot([i for i in range(1,len(btc_otc)+1)], btc_otc, marker='d', ms=ms_size, mec='black', mew=1, label=r'Bitcoin-OTC', linewidth=2, linestyle='dashed')
# ax1.plot([i for i in range(1,len(dblp)+1)], dblp, marker='v', ms=ms_size, mec='black', mew=1, label=r'DBLP', linewidth=2, linestyle='dashed')
# ax1.plot([i for i in range(1,len(reddit)+1)], reddit, marker='^', ms=ms_size, mec='black', mew=1, label=r'Reddit-title', linewidth=2, linestyle='dashed')
# ax1.plot([i for i in range(1,len(uci)+1)], uci, marker='x', ms=ms_size, mec='black', mew=1, label=r'UCI', linewidth=2, linestyle='dashed')

#ax1.legend(fontsize=legend_font_size, loc='upper center', bbox_to_anchor=(1, 1.3), ncol=3)  # 让图例生效
# plt.xticks([i for i in np.arange(0.1,1.1,0.2)], fontsize=x_trick_font_size)
# ax1.set_xticklabels(dims_name)
# ax1.tick_params(labelsize=x_trick_font_size)
# ax1.set_xticks([64, 128, 256, 512])
ax1.margins(margins)
ax1.set_xlabel(u"Snapshots", fontsize=ylabel_font_size) #X轴标签
ax1.set_xlim((0, 265))
# plt.yticks(y_tick11, fontsize=y_trick_font_size)
#ax1.set_ylabel("Density", fontsize=ylabel_font_size) #Y轴标签
ax1.set_title("", fontsize=title_font_size) #标题
ax1.tick_params(labelsize=y_trick_font_size, direction='in', length=5, width=1)

ax1.set_ylim((2e-6, 2.5e-4))
#ax1.set_yticks(np.arange(0.35, 0.66, 0.1))
ax1.grid()

ax2 = fig.add_subplot(133)
ax2.ticklabel_format(style='sci', scilimits=(0,0), axis='y')

ax2.plot([i for i in range(1,len(btc_alpha)+1)], btc_alpha, mew=1, label=u'Bitcoin-Alpha', linewidth=3)
ax2.plot([-1], [-1], mew=1, label=u'Bitcoin-OTC', linewidth=3)
ax2.plot([-1], [-1], mew=1, label=u'DBLP', linewidth=3)
ax2.plot([-1], [-1], mew=1, label=u'Reddit-title', linewidth=3)
ax2.plot([-1], [-1], mew=1, label=u'Stack Overflow', linewidth=3)
ax2.plot([i for i in range(1,len(uci)+1)], uci, mew=1, label=u'UCI', linewidth=3)

# ax1.plot([i for i in range(1,len(btc_alpha)+1)], btc_alpha, marker='o', ms=ms_size, mec='black', mew=1, label=r'Bitcoin-Alpha', linewidth=2, linestyle='dashed')
# ax1.plot([i for i in range(1,len(btc_otc)+1)], btc_otc, marker='d', ms=ms_size, mec='black', mew=1, label=r'Bitcoin-OTC', linewidth=2, linestyle='dashed')
# ax1.plot([i for i in range(1,len(dblp)+1)], dblp, marker='v', ms=ms_size, mec='black', mew=1, label=r'DBLP', linewidth=2, linestyle='dashed')
# ax1.plot([i for i in range(1,len(reddit)+1)], reddit, marker='^', ms=ms_size, mec='black', mew=1, label=r'Reddit-title', linewidth=2, linestyle='dashed')
# ax1.plot([i for i in range(1,len(uci)+1)], uci, marker='x', ms=ms_size, mec='black', mew=1, label=r'UCI', linewidth=2, linestyle='dashed')

# ax1.legend(fontsize=legend_font_size, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, fancybox=True, shadow=True)  # 让图例生效
# plt.xticks([i for i in np.arange(0.1,1.1,0.2)], fontsize=x_trick_font_size)
# ax1.set_xticklabels(dims_name)
# ax1.tick_params(labelsize=x_trick_font_size)
# ax1.set_xticks([64, 128, 256, 512])
ax2.margins(margins)
ax2.set_xlabel(u"Snapshots", fontsize=ylabel_font_size) #X轴标签
ax2.set_xlim((0, 230))
# plt.yticks(y_tick11, fontsize=y_trick_font_size)
#ax1.set_ylabel("Number of edges", fontsize=ylabel_font_size) #Y轴标签
#ax1.set_title("", fontsize=title_font_size) #标题
ax2.tick_params(labelsize=y_trick_font_size, direction='in', length=5, width=1)

ax2.set_ylim((1e-4, 3.5e-3))
#ax1.set_yticks(np.arange(0.35, 0.66, 0.1))
ax2.grid()

plt.tight_layout()
plt.savefig("density.png")
plt.show()


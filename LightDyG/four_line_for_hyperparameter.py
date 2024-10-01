#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os

#acc、ap、f1、mac_auc、mic_auc、mrr、rc1、rc3、rc10
metric_idx = {
    "acc":0,
    "ap":1,
    "auc":3,
    "mrr":5,
    "rc10":8
}

fn_rho = 'LightDyG/beta_0.1_to_0.9.npy'
fn_droprate = 'LightDyG/drop_rate_0.1_to_0.9.npy'
fn_emb_dim = 'LightDyG/out_dim_32_64_128_256.npy'
fn_win_size = 'LightDyG/win_num_4_to_20.npy'

#settings 
legend_font_size = 18
margins = 0.15
ylabel_font_size = 18
title_font_size = 24
y_trick_font_size = 20
x_trick_font_size = 20
ms_size = 8
plt.rc('font',family='Times New Roman')
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["font.weight"] = "bold"



rho_data_raw = np.load(fn_rho)
rho_auc = rho_data_raw[:,metric_idx["auc"]]
rho_mrr = rho_data_raw[:,metric_idx["mrr"]]
rho_acc = rho_data_raw[:,metric_idx["acc"]]
rho_rca = rho_data_raw[:,metric_idx["rc10"]]
rhos = [ i for i in np.arange(0.1, 1.0, 0.1)]

x = rhos
fig = plt.figure(num=1, figsize=(32, 5))
ax1 = fig.add_subplot(141)

ax1.plot(x, rho_auc, marker='o', ms=ms_size, mec='black', mew=1, label=r'AUC', linewidth=2, linestyle='dashed')
ax1.plot(x, rho_mrr, marker='d', ms=ms_size, mec='black', mew=1, label=r'MRR', linewidth=2, linestyle='dashed')
ax1.plot(x, rho_acc, marker='v', ms=ms_size, mec='black', mew=1, label=r'Acc', linewidth=2, linestyle='dashed')
ax1.plot(x, rho_rca, marker='^', ms=ms_size, mec='black', mew=1, label=r'R@10', linewidth=2, linestyle='dashed')
#ax1.legend(fontsize=legend_font_size, loc="upper right")  # 让图例生效
plt.xticks([i for i in np.arange(0.1,1.1,0.2)], fontsize=x_trick_font_size)
# ax1.set_xticklabels(dims_name)
# ax1.tick_params(labelsize=x_trick_font_size)
# ax1.set_xticks([64, 128, 256, 512])
ax1.margins(margins)
ax1.set_xlabel(r"(a) $\tau$", fontsize=ylabel_font_size) #X轴标签
# plt.yticks(y_tick11, fontsize=y_trick_font_size)
ax1.set_ylabel("", fontsize=ylabel_font_size) #Y轴标签
ax1.set_title("", fontsize=title_font_size) #标题
ax1.tick_params(labelsize=y_trick_font_size, direction='in', length=5, width=1)
ax1.set_ylim((0.0, 1.0))
#ax1.set_yticks(np.arange(0.35, 0.66, 0.1))
ax1.grid()


# subfig 2 
droprate_data_raw = np.load(fn_droprate)
dr_auc = droprate_data_raw[:,metric_idx["auc"]]
dr_mrr = droprate_data_raw[:,metric_idx["mrr"]]
dr_acc = droprate_data_raw[:,metric_idx["acc"]]
dr_rca = droprate_data_raw[:,metric_idx["rc10"]]
droprates = [ i for i in np.arange(0.1, 1.0, 0.1)]

x = droprates
ax2 = fig.add_subplot(142)

ax2.plot(x, dr_auc, marker='o', ms=ms_size, mec='black', mew=1, label=r'AUC', linewidth=2, linestyle='dashed')
ax2.plot(x, dr_mrr, marker='d', ms=ms_size, mec='black', mew=1, label=r'MRR', linewidth=2, linestyle='dashed')
ax2.plot(x, dr_acc, marker='v', ms=ms_size, mec='black', mew=1, label=r'Acc', linewidth=2, linestyle='dashed')
ax2.plot(x, dr_rca, marker='^', ms=ms_size, mec='black', mew=1, label=r'R@10', linewidth=2, linestyle='dashed')
#ax2.legend(fontsize=legend_font_size, loc="upper right")  # 让图例生效
plt.xticks([i for i in np.arange(0.1,1.1,0.2)], fontsize=x_trick_font_size)
# ax1.set_xticklabels(dims_name)
# ax1.tick_params(labelsize=x_trick_font_size)
# ax1.set_xticks([64, 128, 256, 512])
ax2.margins(margins)
ax2.set_xlabel(u"(b) Droprate", fontsize=ylabel_font_size) #X轴标签
# plt.yticks(y_tick11, fontsize=y_trick_font_size)
ax2.set_ylabel("", fontsize=ylabel_font_size) #Y轴标签
ax2.set_title("", fontsize=title_font_size) #标题
ax2.tick_params(labelsize=y_trick_font_size, direction='in', length=5, width=1)
ax2.set_ylim((0.0, 1.0))
#ax1.set_yticks(np.arange(0.35, 0.66, 0.1))
ax2.grid()

# subfig 3
emb_dim_data_raw = np.load(fn_emb_dim)
emb_auc = emb_dim_data_raw[:,metric_idx["auc"]]
emb_mrr = emb_dim_data_raw[:,metric_idx["mrr"]]
emb_acc = emb_dim_data_raw[:,metric_idx["acc"]]
emb_rca = emb_dim_data_raw[:,metric_idx["rc10"]]
dims = [1, 2, 3, 4]
dims_name = [
    u"32",
    u"64",
    u"128",
    u"256",
    ]

x = dims
ax3 = fig.add_subplot(143)

ax3.plot(x, emb_auc, marker='o', ms=ms_size, mec='black', mew=1, label=r'AUC', linewidth=2, linestyle='dashed')
ax3.plot(x, emb_mrr, marker='d', ms=ms_size, mec='black', mew=1, label=r'MRR', linewidth=2, linestyle='dashed')
ax3.plot(x, emb_acc, marker='v', ms=ms_size, mec='black', mew=1, label=r'Acc', linewidth=2, linestyle='dashed')
ax3.plot(x, emb_rca, marker='^', ms=ms_size, mec='black', mew=1, label=r'R@10', linewidth=2, linestyle='dashed')
#ax3.legend(fontsize=legend_font_size, loc="upper right")  # 让图例生效
plt.xticks(x, fontsize=x_trick_font_size)
ax3.set_xticklabels(dims_name)
# ax1.tick_params(labelsize=x_trick_font_size)
# ax1.set_xticks([64, 128, 256, 512])
ax3.margins(margins)
ax3.set_xlabel(u"(c) Embedding dimension", fontsize=ylabel_font_size) #X轴标签
# plt.yticks(y_tick11, fontsize=y_trick_font_size)
ax3.set_ylabel("", fontsize=ylabel_font_size) #Y轴标签
ax3.set_title("", fontsize=title_font_size) #标题
ax3.tick_params(labelsize=y_trick_font_size, direction='in', length=5, width=1)
ax3.set_ylim((0.0, 1.0))
#ax1.set_yticks(np.arange(0.35, 0.66, 0.1))
ax3.grid()

# sugfig 4
win_size_data_raw = np.load(fn_win_size)
win_auc = win_size_data_raw[:,metric_idx["auc"]]
win_mrr = win_size_data_raw[:,metric_idx["mrr"]]
win_acc = win_size_data_raw[:,metric_idx["acc"]]
win_rca = win_size_data_raw[:,metric_idx["rc10"]]
wins = [ i for i in np.arange(4, 20, 1)]

x = wins
ax4 = fig.add_subplot(144)

ax4.plot(x, win_auc, marker='o', ms=ms_size, mec='black', mew=1, label=r'AUC', linewidth=2, linestyle='dashed')
ax4.plot(x, win_mrr, marker='d', ms=ms_size, mec='black', mew=1, label=r'MRR', linewidth=2, linestyle='dashed')
ax4.plot(x, win_acc, marker='v', ms=ms_size, mec='black', mew=1, label=r'Acc', linewidth=2, linestyle='dashed')
ax4.plot(x, win_rca, marker='^', ms=ms_size, mec='black', mew=1, label=r'R@10', linewidth=2, linestyle='dashed')
ax4.legend(fontsize=legend_font_size, bbox_to_anchor=(1.02, 0.3), loc=3, borderaxespad=0)  # 让图例生效
plt.xticks([i for i in np.arange(4, 21, 4)], fontsize=x_trick_font_size)
# ax1.set_xticklabels(dims_name)
# ax1.tick_params(labelsize=x_trick_font_size)
# ax1.set_xticks([64, 128, 256, 512])
ax4.margins(margins)
ax4.set_xlabel(u"(d) Window size", fontsize=ylabel_font_size) #X轴标签
# plt.yticks(y_tick11, fontsize=y_trick_font_size)
ax4.set_ylabel("", fontsize=ylabel_font_size) #Y轴标签
ax4.set_title("", fontsize=title_font_size) #标题
ax4.tick_params(labelsize=y_trick_font_size, direction='in', length=5, width=1)
ax4.set_ylim((0.0, 1.0))
#ax1.set_yticks(np.arange(0.35, 0.66, 0.1))
ax4.grid()

# plt.tight_layout()
plt.savefig("hyperprara.png")
plt.show()


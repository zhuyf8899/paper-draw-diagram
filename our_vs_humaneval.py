import matplotlib.pyplot as plt

# 数据，模型名称和对应的 DSB 和 HumanEval 的 Pass@1 值
models = [
    'o1-mini', 
    "GPT-4o", 'GPT-4o-mini','GPT-4-Turbo', 'Claude-3-5-S', "GLM-4-Flash", 
    "Llama-3.1-8B-I", "Llama-3-8B-I", 
    "gemma-2-9b-it", "GLM-4-9b-Chat", "Qwen2.5-7B-I", 
    "Qwen2-7B-I", "Qwen2-1.5B-I", "Yi-1.5-9B-Chat-16K",
    "CodeLlama-34b-I", "CodeLlama-13b-I", "CodeLlama-7b-I", "StarCoder2-15b", 
    "Deepseek-Coder-33b-I", "Deepseek-Coder-6.7b-I",  "Deepseek-Coder-1.3b-I",  
    "Qwen2.5-Coder-7B-I", "Qwen2.5-Coder-1.5B-I",
]

pass_humaneval = [
    92.4, 90.2, 87.2, 85.4, 92.0, 56.1, 59.5, 62.2, 63.7, 71.8, 
    79.4, 65.3, 28.2, 57.6, 41.5, 42.7, 34.8, 46.3, 69.2, 66.1, 
    48.4, 80.5, 57.2
]

pass_dsb = [
    29.06, 64.96, 49.64, 50.85, 46.98, 29.91, 24.28, 2.88, 6.44, 25.14, 
    43.15, 22.38, 3.69, 37.79, 0.90, 10.45, 2.88, 2.02, 55.23, 36.49, 
    15.36, 44.82, 22.47
]

# 设置样式
# plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(12, 8))

markers = [
    'o', 'o', 'o', 'o', 'o', 'o', 
    'P', 'P', '^', 'X', '^', '^', 
    '^', 'h', 's', 's', 's', 'h', 
    'D', 'D', 'D', 'o', 'o'
]

colors = [
    'black', 'cornflowerblue', 'darkorange', 'mediumseagreen', 'tomato', 
    'peru', 'plum', 'gold', 'lightsalmon', 'lightcoral', 'darkkhaki', 
    'indianred', 'deepskyblue', 'hotpink', 'chocolate', 'darkcyan', 
    'lavender', 'teal', 'violet', 'sandybrown', 'firebrick',
    'royalblue', 'limegreen', 'orangered'
]


# 绘制散点图
for i, model in enumerate(models):
    ax.scatter(pass_dsb[i], pass_humaneval[i], marker=markers[i], color=colors[i], s=100)

# 添加注释，防止重叠
for i, model in enumerate(models):
    offset = 1 if (i % 2 == 0) else -2
    if model == 'Llama-3-8B-I' or model == 'StarCoder2-15b' or model == 'CodeLlama-34b-I' :
        ax.text(pass_dsb[i] + 0.5 + offset, pass_humaneval[i] + 0.5 + offset, model, fontsize=9, ha='left')
    else:
        ax.text(pass_dsb[i] + 0.5 + offset, pass_humaneval[i] + 0.5 + offset, model, fontsize=9, ha='right')


# 标签和标题
ax.set_xlabel('Pass@1 on DataSciBench', fontsize=15)
ax.set_ylabel('Pass@1 on HumanEval', fontsize=15)
ax.set_title('DataSciBench vs HumanEval', fontsize=18)

# 设置y轴的最小值为23
ax.set_ylim(bottom=23)
# 设置x轴的最小值为23
ax.set_xlim(right=75)

# 调整后的线条分区
# 确保线条在新区域的对角线上
ax.plot([-2, 80], [23, 100], color=(229 / 255, 204 / 255, 255 / 255), linestyle='--', linewidth=5)
# 设置x轴和y轴的刻度线数值的大小
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)


# 设置图例
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='lower center', fontsize=8, ncol=6, bbox_to_anchor=(0.5, 1.05))

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
plt.savefig('DSB_vs_HumanEval.pdf', dpi=300)
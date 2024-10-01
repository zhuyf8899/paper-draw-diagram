import matplotlib.pyplot as plt
import numpy as np

# 数据
models = [
    "Qwen2.5-Coder-1.5B-I",
    "Qwen2.5-Coder-7B-I",
    "Deepseek-Coder-1.3b-I",
    "Deepseek-Coder-6.7b-I",
    "Deepseek-Coder-33b-I",
    "StarCoder2-15b",
    "CodeLlama-7b-I",
    "CodeLlama-13b-I",
    "CodeLlama-34b-I",
    "Yi-1.5-9B-Chat-16K",
    "Qwen2-1.5B-I",
    "Qwen2-7B-I",
    "Qwen2.5-7B-I",
    "GLM-4-9b-chat",
    "gemma-2-9b-it",
    "Llama-3-8B-I",
    "Llama-3.1-8B-I",
    "GLM-4-flash",
    "claude-3-5-s",
    "gpt-4-turbo",
    "gpt-4o-mini",
    "gpt-4o",
    "o1-mini"
]
scores = [
    25.89,
    47.67,
    16.55,
    38.42,
    56.74,
    2.45,
    3.32,
    12.84,
    1.33,
    38.28,
    4.84,
    23.54,
    45.99,
    27.57,
    12.69,
    3.40,
    29.70,
    30.75,
    52.26,
    54.59,
    54.12,
    64.43,
    38.73
]
access_types = ['Open Access']*17 + ['API Access']*6

# 分开API Access和Open Access数据
api_indices = [i for i, access in enumerate(access_types) if access == 'API Access']
open_indices = [i for i, access in enumerate(access_types) if access == 'Open Access']

# 对各自类别的数据进行降序排列
sorted_api_indices = [i for _, i in sorted(zip([scores[i] for i in api_indices], api_indices), reverse=False)]
sorted_open_indices = [i for _, i in sorted(zip([scores[i] for i in open_indices], open_indices), reverse=False)]

# 合并排序后的索引
sorted_indices = sorted_open_indices + sorted_api_indices

# 根据排序后的顺序重新排列数据
models = [models[i] for i in sorted_indices]
scores = [scores[i] for i in sorted_indices]
access_types = [access_types[i] for i in sorted_indices]

# 更新颜色
colors = ['#d95f02' if access == 'Open Access' else '#7570b3' for access in access_types]

# 创建图形
fig, ax = plt.subplots(figsize=(28, 8))

# 创建条形图
y_pos = np.arange(len(models))
bars = ax.barh(y_pos, scores, color=colors)
 
# 添加文字标签
for bar in bars:
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
            '       %.2f' % bar.get_width(),
            ha='center', va='center', fontsize=16)
# Y轴标签
ax.set_yticks(y_pos)
ax.set_yticklabels(models, fontsize=18)

# X轴标签
ax.set_xlabel('Pass@1', fontsize=18)
ax.set_title('DataSciBench', fontsize=25)

# 分区背景颜色
ax.axhline(y=len(open_indices) - 0.5, color='k', linewidth=4)
plt.text(60, len(open_indices) + 3, 'API Access', fontsize=20, va='center', ha='center', backgroundcolor='#7570b3')
plt.text(60, (len(open_indices) - 0.5) / 2, 'Open Access', fontsize=20, va='center', ha='center', backgroundcolor='#d95f02')

# 计算平均值
open_access_scores = [score for score, access in zip(scores, access_types) if access == 'Open Access']
api_access_scores = [score for score, access in zip(scores, access_types) if access == 'API Access']

open_access_avg = np.mean(open_access_scores)
api_access_avg = np.mean(api_access_scores)

# 绘制平均线
ax.axvline(x=open_access_avg, color='#d95f02', linestyle='--')
ax.axvline(x=api_access_avg, color='#7570b3', linestyle='--')

# 添加平均数值标签
ax.text(open_access_avg + 3, 0.8, f'Avg: {open_access_avg:.2f}', color='#d95f02', ha='center', fontsize=20)
ax.text(api_access_avg + 3, max(y_pos) + 0.5, f'Avg: {api_access_avg:.2f}', color='#7570b3', ha='center', fontsize=20)

# 显示图形
plt.show()
plt.savefig('all_models.pdf')
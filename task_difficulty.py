import matplotlib.pyplot as plt
import numpy as np

# 模型名称
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

# Easy, Medium 和 Hard 的通过率
easy = [
    51.62, 78.35, 65.85, 67.21, 67.60,
    39.31, 39.18, 4.43, 11.99, 34.75,
    59.29, 29.32, 6.18, 50.11, 1.76,
    17.53, 4.72, 3.09, 70.93, 47.20,
    22.79, 62.40, 32.76
]

medium = [
    8.38, 15.91, 14.79, 15.57, 9.88,
    8.25, 6.85, 1.28, 2.28, 7.57,
    8.27, 5.48, 1.52, 4.44, 0.06,
    0.70, 0.49, 0.18, 11.92, 11.77,
    0.46, 6.73, 8.07
]

hard = [
    13.97, 14.46, 11.37, 8.80, 4.20,
    1.57, 3.78, 0.00, 1.98, 1.59,
    1.08, 0.51, 0.25, 0.37, 0.00,
    0.19, 0.05, 0.23, 8.07, 8.98,
    0.00, 2.69, 3.84
]



# 设置条形的宽度和位置
bar_width = 0.30
index = np.arange(len(models))

# 创建条形图
fig, ax = plt.subplots(figsize=(15, 8))
bars1 = ax.bar(index, easy, bar_width, label='easy', color='#7570b3')
bars2 = ax.bar(index + bar_width, medium, bar_width, label='medium', color='#1F77B4')
bars3 = ax.bar(index + bar_width * 2, hard, bar_width, label='hard', color='#d95f02')

# 计算每个难度的平均值
easy_avg = np.mean(easy)
medium_avg = np.mean(medium)
hard_avg = np.mean(hard)

# 绘制平均线
ax.axhline(y=easy_avg, color='#7570b3', linestyle='--')
ax.axhline(y=medium_avg,  linestyle='--')
ax.axhline(y=hard_avg, color='#d95f02', linestyle='--')

# 添加平均数值标签
ax.text(len(models) - 6.9, easy_avg, f'Avg: {easy_avg:.2f}', color='#7570b3', fontsize=12, va='center', ha='left', backgroundcolor='white')
ax.text(len(models) - 6.7, medium_avg, f'Avg: {medium_avg:.2f}', color='#1F77B4', fontsize=11, va='center', ha='left', backgroundcolor='white')
ax.text(len(models) - 9.45, hard_avg, f'Avg: {hard_avg:.2f}', color='#d95f02', fontsize=10, va='center', ha='left', backgroundcolor='white')

# 添加标题和标签
ax.set_xlabel('Model Name', fontsize=20)
ax.set_ylabel('Ave. CR', fontsize=20)
ax.set_title('Different Difficulty Level for Data Science', fontsize=20)
ax.set_xticks(index + bar_width)
ax.set_xticklabels(models, rotation=45, ha='right', fontsize=15)
ax.tick_params(axis='y', labelsize=18)

# 添加图例
ax.legend(loc='upper center', fontsize=20, ncol=3)

# 显示每个条形的数值
def add_labels(bars, values):
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax.annotate(f'{value:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=12)

# add_labels(bars1, easy)
# add_labels(bars2, medium)
# add_labels(bars3, hard)

# 调整布局，使x轴标签不重叠
plt.tight_layout()

# 显示图形
plt.show()
plt.savefig('task_difficulty.pdf')
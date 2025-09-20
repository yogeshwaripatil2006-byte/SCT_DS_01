import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style='whitegrid')

# Load data from GitHub
url = 'https://github.com/vmahamear/data-science-datasets-collection/raw/main/mall_customers.csv'
df = pd.read_csv(url)

# 1. Categorical Distribution: Gender
plt.figure(figsize=(6, 4))
palette = sns.color_palette('pastel')
ax = sns.countplot(x='Gender', data=df, palette=palette)
plt.title('Number of Customers by Gender', fontsize=14)
plt.xlabel('Gender')
plt.ylabel('Count')

# Annotate bars
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height}', (p.get_x() + p.get_width() / 2, height + 1),
                ha='center', fontsize=12)

plt.tight_layout()
plt.show()

# 2. Continuous Distribution: Age - Histogram + KDE
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=15, kde=True, color='skyblue')
plt.title('Age Distribution of Customers', fontsize=14)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

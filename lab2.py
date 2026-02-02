import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
california_data = fetch_california_housing(as_frame=True)
data=california_data.frame
cooreleation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(cooreleation_matrix, annot=True, cmap='coolwarm', fmt=".2f",linewidths=1.5)
plt.title('Correlation Matrix for California Housing Feature')
plt.show()
sns.pairplot(data, diag_kind='kde', plot_kws={'alpha':0.5})
plt.suptitle('Pairplot for California Housing Features', y=1.02)
plt.show()
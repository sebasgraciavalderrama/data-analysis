import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_palette('deep')

tips = sns.load_dataset('tips')
tips.head()
sns.displot(tips['total_bill'], kde=True, bins=30) # Distribution or histogram
plt.show()
sns.jointplot(x='total_bill', y='tip', data=tips)
plt.show()
sns.pairplot(tips, hue='sex', palette='coolwarm')
plt.show()
sns.rugplot(tips['total_bill'])
plt.show()


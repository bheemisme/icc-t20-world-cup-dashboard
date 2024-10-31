import seaborn as sns
import matplotlib.pyplot as plt
from analytics.preprocessing import *

fig, axs = plt.subplots()
sns.countplot(data=match, y='Winners', hue='Method', ax=axs)
fig.suptitle("Winners by Method")

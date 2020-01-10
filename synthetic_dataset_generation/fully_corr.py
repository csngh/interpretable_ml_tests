import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence
from sklearn.decomposition import PCA

# Creating features
x1 = [np.random.normal(10, 2) for x in range(1000)]
x2 = [(2 * x) + 1 for x in x1]
x3 = [math.sin(x) for x in x1]

# Adding label
y = [x + y + z for (x, y, z) in list(zip(x1, x2, x3))]

# Creating Dataframe
df = pd.DataFrame({"x1": x1, "x2": x2, "x3": x3, "y": y})

# Visualizing Correlations
sns.heatmap(df.corr(method="spearman"), annot=True, vmax=1, vmin=-1)
plt.title("Inter-Correlations between features and labels")

# Visualizing the relations between features and label
plt.scatter(x1, y, c="r", alpha=0.4, label="X1: Gaussian Dist")
plt.scatter(x2, y, c="b", alpha=0.4, label="X2: 2X1 + 1")
plt.scatter(x3, y, c="y", alpha=0.4, label="X3: sin(X1)")
plt.legend()
plt.title("Scatter Plot of Relations between Features and Label")
plt.xlabel("Features")
plt.ylabel("Outcome")

# Cleaning up
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
stdx = StandardScaler()
X = stdx.fit_transform(X)

# Building Model
est = RandomForestRegressor()
est.fit(X, y)

# Analyzing PDP plots
features = [0, 1]
plot_partial_dependence(est, X, features)

# PCA
pca = PCA(n_components=2, whiten=True)
X = pca.fit(X).transform(X)

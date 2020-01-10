import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence
from sklearn.model_selection import train_test_split

# Creting Dataset (M1, M2 and R)
m1 = []
m2 = []
r = []
for i in range(1000):
    # Smaller Object
    m1.append(np.random.randint(1, 100))
    # Bigger Object
    m2.append(np.random.randint(5000, 10000))
    # Radius between Objects
    r.append(np.random.randint(1, 1000) / 10)

# Generating Equation
gravitation_constant = 6.67 * (10 ** (-1))
force = []
for i in range(1000):
    f = gravitation_constant * m1[i] * m2[i] / (r[i] ** 2)
    force.append(round(f, 3))

# Visualizing Scatter plot for Outliers
plt.scatter(m1, force)
plt.scatter(m2, force)
plt.xlabel("Mass")
plt.ylabel("Force")
plt.ylim(0, 6e4)

# Creating Dataframe
df = pd.DataFrame({"m1": m1, "m2": m2, "r": r, "F": force})

# Visualizing Correlations
sns.heatmap(df.iloc[:, :-1].corr(), annot=True)

# Removing Outliers and Saving the Dataset to .csv
to_rem = df[df["F"] > 6e4].index.values.tolist()
df.drop(to_rem, inplace=True)

df.to_csv("gravitation.csv")

# Fitting a Model
est = RandomForestRegressor()
x_train, x_test, y_train, y_test = train_test_split(
    df.iloc[:, :-1], df.iloc[:, -1], test_size=0.2
)
print(est.feature_importances_)
est.fit(x_train, y_train)

# Plotting Partial Dependence
plot_partial_dependence(est, df.iloc[:, :-1], ["m1", "m2", "r"])

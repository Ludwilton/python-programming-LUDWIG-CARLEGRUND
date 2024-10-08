import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csv_file = "repos/python-programming-LUDWIG-CARLEGRUND/Labs/unlabelled_data.csv"

data = pd.read_csv(csv_file, header=None)

print(data)
data = np.array(data, dtype=float)

def scatter_plot():
    x = data[:,0]
    y = data[:, 1]
    plt.scatter(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

scatter_plot()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csv_file = "repos/python-programming-LUDWIG-CARLEGRUND/Labs/unlabelled_data.csv"

data = pd.read_csv(csv_file, header=None)

# print(data)
data = np.array(data, dtype=float)
x = data[:, 0]
y = data[:, 1]

# print(x)
k = -0.50  # Lutning
m = 0 # skärningspunkt

y_line = k * x + m

def plot_line():
    plt.scatter(x, y,)
    plt.plot(x, y_line, color="red", label="y=kx+m")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid()
    plt.show()


def classify_points(data=data, k=k, m=m):
    above_line = []
    below_line = []
    
    for row in data:
        x, y = row

        if y > k * x + m:
            above_line.append([x,y])
        else:
            below_line.append([x,y])

    return above_line, below_line


def plot_classified_points():
    above_line, below_line = classify_points()

    x_a = [point[0] for point in above_line]
    y_a = [point[1] for point in above_line]
    
    x_b = [point[0] for point in below_line]
    y_b = [point[1] for point in below_line]

    plt.scatter(x_a, y_a, color="yellow")
    plt.scatter(x_b, y_b, color="blue")

    plt.plot(x, y_line, color="red", label="y=kx+m")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid()
    plt.show()


plot_classified_points()



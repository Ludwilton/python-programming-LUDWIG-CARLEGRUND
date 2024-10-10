import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

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


def classify_points(data=data, k=k, m=m, plot=False):
    above_line = []
    below_line = []
    classified_points = []


    for row in data:
        x, y = row

        if y > k * x + m:
            above_line.append([x,y])
            label = 1
        else:
            below_line.append([x,y])
            label = 0
        
        classified_points.append([x,y,label])

    if plot: # skulle kunna endast använda classified_points för att plotta, skippa above/below, om label == 0, color = "--" osv
        return above_line, below_line
    else:
        return classified_points


def plot_classified_points():
    above_line, below_line = classify_points(plot=True)


    x_a = [point[0] for point in above_line]
    y_a = [point[1] for point in above_line]
    
    x_b = [point[0] for point in below_line]
    y_b = [point[1] for point in below_line]

    plt.scatter(x_a, y_a, color="yellow")
    plt.scatter(x_b, y_b, color="blue")

    plt.plot(x, y_line, color="red", label="separator")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid()
    plt.show()


plot_classified_points()

classified_data = classify_points()
classified_data = np.array(classified_data, dtype=float)
print(classified_data)

with open("repos/python-programming-LUDWIG-CARLEGRUND/Labs/labelled_data.csv", "w") as w_file:
    csv_writer = csv.writer(w_file)

    for row in classified_data:
        csv_writer.writerow(row)

plot_line()

def plot_classified_points_2():
    data = classify_points()
    data = np.array(data, dtype=float)
    x = data[:, 0]
    y = data[:, 1]
    l = data[:, 2]
    plt.scatter(x[l == 0], y[l==0], color="red", label="0")
    plt.scatter(x[l == 1], y[l==1], color="blue", label="1")
    plt.plot(x, y_line, color="red", label="y=kx+m")
    plt.show()

plot_classified_points_2()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv


def get_data():
    csv_file = "repos/python-programming-LUDWIG-CARLEGRUND/Labs/unlabelled_data.csv"

    data = pd.read_csv(csv_file, header=None)
    data = np.array(data, dtype=float)
    return data


def get_default_k():
    return -.5  # Lutning 


def get_default_m():
    return 0 # skärningspunkt


def plot_line(data=get_data(), k=get_default_k(), m=get_default_m()):
    x = data[:, 0]
    y = data[:, 1]
    y_line = k * x + m
    plt.scatter(x, y,)
    plt.plot(x, y_line, color="red", label="y=kx+m")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid()
    plt.show()


def classify_points(data=get_data(), k=get_default_k(), m=get_default_m()):
    classified_points = []

    for row in data:
        x, y = row

        if y > k * x + m:
            label = 1
        else:
            label = 0
        
        classified_points.append([x,y,label])
    return classified_points


def classify_and_write_labels():
    classified_data = classify_points()
    classified_data = np.array(classified_data, dtype=float)
    print(classified_data)

    with open("repos/python-programming-LUDWIG-CARLEGRUND/Labs/labelled_data.csv", "w") as w_file:
        csv_writer = csv.writer(w_file)

        for row in classified_data:
            csv_writer.writerow(row)
    print(f"data classified and saved to {w_file}")


def plot_classified_points_2(k = get_default_k(), m = get_default_m()):
    data = classify_points()
    data = np.array(data, dtype=float)
    x = data[:, 0]
    y = data[:, 1]
    l = data[:, 2]
    y_line = k * x + m
    plt.scatter(x[l == 0], y[l==0], color="yellow", label="0")
    plt.scatter(x[l == 1], y[l==1], color="blue", label="1")
    plt.plot(x, y_line, color="red", label="separator")
    plt.ylim(-5, 5)
    plt.xlim(-5, 5)
    plt.show()

plot_line()
plot_classified_points_2()
classify_and_write_labels()
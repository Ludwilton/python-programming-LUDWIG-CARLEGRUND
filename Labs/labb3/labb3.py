import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import os

def get_default_k():
    return -.5  # Lutning 


def get_default_m():
    return 0 # skärningspunkt


def get_data():
    path = os.path.dirname(__file__) + "/unlabelled_data.csv"
    csv_file = path

    data = pd.read_csv(csv_file, header=None)
    data = np.array(data, dtype=float)
    return data




def classify_data_points(data=get_data(), k=get_default_k(), m=get_default_m()):
    classified_points = []
    count_1 = 0
    count_0 = 0

    for row in data:
        x, y = row

        if y > k * x + m:
            label = 1
            count_1 += 1
        else:
            label = 0
            count_0 += 1
        
        classified_points.append([x,y,label])

    print(f"Data för linje med lutning: {k}, skärningspunkt {m}")
    print(f"Antal punkter till höger om linjen: {count_1}")
    print(f"Antal punkter till vänster om linjen: {count_0}")
    return classified_points


def write_classified_data_csv(k = get_default_k(), m = get_default_m()):
    classified_data = classify_data_points(k=k, m=m)
    classified_data = np.array(classified_data, dtype=float)
    print(classified_data)
    path = os.path.dirname(__file__) + "/labelled_data.csv"
    print(path)
    with open(path, "w") as w_file:
        csv_writer = csv.writer(w_file)

        for row in classified_data:
            csv_writer.writerow(row)
    print(f"data classified and saved to {w_file}")


def plot_classified_points(k = get_default_k(), m = get_default_m(), axes=None, color="red", label="separator line"):
    data = classify_data_points(k=k, m=m)
    data = np.array(data, dtype=float)
    x = data[:, 0]
    y = data[:, 1]
    l = data[:, 2]
    y_line = k * x + m

    axes.scatter(x[l == 0], y[l==0], color="gold")
    axes.scatter(x[l == 1], y[l==1], color="cyan")
    axes.set_ylabel("y")
    axes.set_xlabel("x")
    axes.plot(x, y_line, color=color, label=label)
    axes.set(ylim = (-5, 5), xlim = (-5, 5))


if __name__ == "__main__":
    axes = plt.axes()
    plot_classified_points(axes=axes) # defaultvärden
    plot_classified_points(k=800, m=-120, axes=axes)
    plot_classified_points(k=-0.489, axes=axes)
    plot_classified_points(k=-2, m=0.16, axes=axes)
    plt.grid()
    plt.show()
    # write_classified_data_csv()
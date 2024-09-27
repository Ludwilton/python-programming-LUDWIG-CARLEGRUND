import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import os
print(os.getcwd())
csv_file = "/Users/luddecmc/Desktop/SKOLARBETE-ITHS/repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.csv"

test_points = [
    [25, 32],
    [24.2, 31.5],
    [22, 34],
    [20.5, 34]
]

def txt_to_csv():
    with open("repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.txt", "r") as txt_file:
        lines = txt_file.readlines()

    with open("repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.csv", "w") as csv_file:

        csv_write = csv.writer(csv_file)

        for line in lines[1:]:
            row = line.strip().split(", ")
            csv_write.writerow(row)
    


def plot_csv(csv_file):
    csv_data = pd.read_csv(csv_file, names=["width cm", "height cm", "label"])
    width = csv_data["width cm"]
    height = csv_data["height cm"]
    label = csv_data["label"]
    plt.scatter(width[label == 0], height[label == 0],label="pichu", alpha=0.7)
    plt.scatter(width[label == 1], height[label == 1],label="pikachu", alpha=0.7)
    plt.xlabel("width")
    plt.ylabel("height")
    plt.title("pichu vs pikachu in sizes")
    plt.legend()
    plt.show()


def euc_distance(a):
    return np.sqrt(np.sum((a - b) ** 2))


def calc_distances():
    with open(csv_file, "r") as data:
        lines = data.readlines()

    data = []
    for line in lines:
        row = line.strip().split(",")
        data.append(row)
    data_points = [row[:2] for row in data]
    print(data_points)
    label_points = [row[2:] for row in data]
    print(label_points)
    data = np.array(data_points, dtype=float)
    print(data)
    


# txt_to_csv()
# plot_csv(csv_file)
calc_distances()
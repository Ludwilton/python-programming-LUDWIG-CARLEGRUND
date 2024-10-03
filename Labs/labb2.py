import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import os
import random as rng
print(os.getcwd())
csv_file = "/Users/luddecmc/Desktop/SKOLARBETE-ITHS/repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.csv"

test_points = [
    [25, 32],
    [24.2, 31.5],
    [22, 34],
    [20.5, 34]
]

k = 1


with open(csv_file, "r") as data:
    lines = data.readlines()
data = []
for line in lines:
    row = line.strip().split(",")
    data.append(row)


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


def euc_distance(a,b):
    return np.sqrt(np.sum((a - b) ** 2))


def calc_distances(test_points = test_points, data = data, k = k):

    data = np.array(data, dtype=float)
    test_points = np.array(test_points, dtype=float)


    print(test_points)
    k_lowest_each_point = []
    
    # jämför testpunkter mot datapunkter, passar även vidare klass för varje datapunkt
    for i, test_point in enumerate(test_points):
        print(f"\nAvstånd för test point: {i+1} {test_point}")
        

        distances = [(euc_distance(test_point, data_point[:2]), data_point[2]) for data_point in data]

        
        for c, j in enumerate(distances):
            print(f"avstånd mellan TP:{i+1} och DP:{c+1} {j}")
        
        sorted_distances = sorted(distances, key=lambda x: x[0])
        k_lowest_each_point.append(sorted_distances[0:k])

    
    for c, neighbors in enumerate(k_lowest_each_point): 
        labels = [neighbor[1] for neighbor in neighbors]
        tp_class = round(sum(labels) / k)
        if tp_class == 1:
            print(f"test punkt {c+1} är pikachu")
        else:
            print(f"test punkt {c+1} är pichu")
        


def scramble_dataset(data = data):
    pichu_list = []
    pikachu_list = []
    for i in data:
        if i[2] == "0":
            pichu_list.append(i)
        else:
            pikachu_list.append(i)

    

    pikachu_list = np.array(pikachu_list, dtype=float)
    pichu_list = np.array(pichu_list, dtype=float)
    # lista i lista?
    # print(pichu_list)
    # print(pikachu_list)
    pichu_random = np.random.permutation(pichu_list)
    pikachu_random = np.random.permutation(pikachu_list)
    
    test_points = np.concatenate((pichu_list[50:, :2], pikachu_random[50:, :2]), axis=0)
    data_points = np.concatenate((pichu_random[:50], pikachu_random[:50]), axis=0)
    
    test_points_randomized = np.random.permutation(test_points)
    data_points_randomized = np.random.permutation(data_points)
    print(len(data_points_randomized))
    # calc_distances(test_points_randomized, data_points_randomized)



def main_menu():

    choices = {
        1: "läs in datapoints och konvertera till .csv",
        2: "plotta datapunkter",
        3: "kalkylera minsta avstånd mellan test och datapunkter, specifiera K",
        4: "slumpa en fördelning på 100/50 av datapunkterna och kalkylera",
     }
    for key, value in choices.items():
        print(f"{key}, {value}") 

    choice = input("Välj ditt val: ")
    while True:
        pass



# txt_to_csv()
# plot_csv(csv_file)
# main_menu()

# calc_distances([[10.5, 20],[18, 23], [30, 32], [10, 20], [12.5, 50]],[[19.332572350434354,32.25325633655492,0],
# [24.73645685241186,35.33291181124776,0],
# [23.79257560586339,38.10372825362463,1],
# [24.557612968127465,36.73144402805611,1],
# [20.191281253428173,35.06966921830237,0],
# [25.813562951888365,35.561029988644336,1],
# [24.923378667802954,34.463907946680294,1],
# [25.311244044578427,34.117212558131975,1],
# [22.819091361866796,34.25516433025548,1],
# [19.639358214988224,34.56117030001663,0],
# [18.341233265627693,31.399261188293124,0],
# [22.723629043769336,34.83845262048311,1],
# [25.82936770950206,33.16210202637511,1],
# [20.23890182459327,32.78945132868386,0],
# [17.905128921789093,28.88813385482529,0],
# [24.385289647525166,37.335669057387726,1],
# [26.525412887538252,35.2192205449002,1]])

# calc_distances()


scramble_dataset()
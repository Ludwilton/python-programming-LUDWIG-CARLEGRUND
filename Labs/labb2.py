import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import os
import random as rng
print(os.getcwd())
csv_file = "repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.csv"

test_points = [
    [25, 32],
    [24.2, 31.5],
    [22, 34],
    [20.5, 34]
]

k = 1 # antal grannar calc_distances kollar mot



def txt_to_csv():
    with open("repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.txt", "r") as txt_file:
        lines = txt_file.readlines()

    with open("repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.csv", "w") as csv_file:
        csv_write = csv.writer(csv_file)

        for line in lines[1:]:
            row = line.strip().split(", ")
            csv_write.writerow(row)
    
txt_to_csv()
with open(csv_file, "r") as data:
    lines = data.readlines()
data = []
for line in lines:
    row = line.strip().split(",")
    data.append(row)



def plot_tp_vs_dp(csv_file=csv_file):
    csv_data = pd.read_csv(csv_file, names=["width cm", "height cm", "label"])
    width = csv_data["width cm"]
    height = csv_data["height cm"]
    label = csv_data["label"]
    plt.scatter(width[label == 0], height[label == 0],label="pichu", alpha=0.7)
    plt.scatter(width[label == 1], height[label == 1],label="pikachu", alpha=0.7)
    plt.xlabel("bredd")
    plt.ylabel("höjd")
    plt.title("pichu vs pikachu beroende på storlek")
    plt.legend()
    plt.show()


def euc_distance(a,b):
    return np.sqrt(np.sum((a - b) ** 2))


def calc_distances(test_points = test_points, data = data, k = k, test_point_classes = True): 
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    data = np.array(data, dtype=float)
    test_points = np.array(test_points, dtype=float) 
    k_lowest_each_point = []
    
    # jämför testpunkter mot datapunkter, passar även vidare klass för varje datapunkt
    for i, test_point in enumerate(test_points): # för varje rad/element i test_points
        
        print(f"Test punkt: {i+1}: {test_point}")
        distances = [(euc_distance(test_point[:2], data_point[:2]), data_point[2]) for data_point in data] # avstånd för varje rad i data_points

        # för att printa avstånd mellan varje test och datapunkt: avkommentera även 3 rader upp.
        # for c, j in enumerate(distances):
            # print(f"avstånd mellan TP:{i+1} och DP:{c+1} {j}")
        
        sorted_distances = sorted(distances, key=lambda x: x[0]) # passar vidare klassifiering 
        k_lowest_each_point.append(sorted_distances[0:k]) # lägger till K antal lägsta för varje test punkt

    for c, neighbors in enumerate(k_lowest_each_point): 
        '''
        note, round rundar neråt om lika många av varje, 
        om te.x k=10 kan denna bli 0.5, en lösning till detta kan vara att ändra vikten av k per iteration.
        ''' 
        labels = [neighbor[1] for neighbor in neighbors]
        tp_class = round(sum(labels) / k)
        if tp_class == 1:
            print(f"test punkt {c+1} är pikachu")
        else:
            print(f"test punkt {c+1} är pichu")
        

        if test_point_classes: # flaggan används när beräkning av medelaccuracy ska ske . . # TODO skulle kunna vara en egen funktion
        # jämför tp_class(0 eller 1) mot test_points klasser -> rad[c] i test_points item = [2]
            if tp_class == 1 and tp_class == test_points[c,2]:
               #True P
               tp += 1
            elif tp_class == 1 and tp_class != test_points[c,2]:
               #False P
               fp += 1
            elif tp_class == 0 and tp_class == test_points[c,2]:
               #True N
               tn += 1
            elif tp_class == 0 and tp_class != test_points[c,2]:
               #False N  
               fn += 1

    if test_point_classes:
        accuracy = (tp + tn) / (tp+tn+fp+fn)
        return accuracy
        

# def plot_accuracy(accuracies, iterations):
#     for iteration, accuracy in enumerate(accuracies):
#         print(f"noggranhet för iteration {iteration+1} = {accuracy}")
#     average_accuracy = sum(accuracies)/iterations
#     print(f"medelaccuracy: {average_accuracy}")
#     plt.plot(iterations, accuracies, marker="o", linestyle="-", color="b", label="accuracy per iteration")
#     plt.title(f"medelaccuracy: {average_accuracy*100:.2f}")
#     plt.xlabel('Iteration', fontsize=12)
#     plt.ylabel('Accuracy', fontsize=12)
#     plt.grid()
#     plt.show()


def plot_accuracy(accuracies, iterations):
    average_accuracy = sum(accuracies) /iterations
    
    
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, accuracies, marker='o', linestyle='-', color='b', label='Accuracy per iteration')
    
    plt.grid(True)
    plt.title(f'Medelaccuracy: {average_accuracy:.2f}', fontsize=16, fontweight='bold')
    plt.xlabel('Iteration', fontsize=12)
    plt.ylabel('Accuracy', fontsize=12)
    
    for i, accuracy in enumerate(accuracies):
        plt.text(iterations[i], accuracies[i] + 0.005, f'{accuracy:.2f}', ha='center', fontsize=10)
    
    plt.axhline(y=average_accuracy, color='r', linestyle='--', label=f'Average accuracy: {average_accuracy:.2f}')
    plt.show()

def scramble_dataset(data = data, k=k, iterations = 10): # delar upp och slumpmässigt delar ut punkter av båda klasser till test/data points med jämn fördelning
    accuracies = []
    for i in range(iterations):
        pichu_list = []
        pikachu_list = []
        for i in data: # sorterar data beroende på klassifiering
            if i[2] == "0": 
                pichu_list.append(i)
            else:
                pikachu_list.append(i)

        pikachu_list = np.array(pikachu_list, dtype=float)
        pichu_list = np.array(pichu_list, dtype=float)

        pichu_random = np.random.permutation(pichu_list) # slumpar innan concat
        pikachu_random = np.random.permutation(pikachu_list)

        test_points = np.concatenate((pichu_random[50:], pikachu_random[50:]), axis=0) # fördelar upp pichu/pikachu klasser 50/25 i data/test
        data_points = np.concatenate((pichu_random[:50], pikachu_random[:50]), axis=0)

        test_points_randomized = np.random.permutation(test_points) # slumpar efter concat, annars är alla pikachu klasser sist i listan
        data_points_randomized = np.random.permutation(data_points)

        accuracy = calc_distances(test_points_randomized, data_points_randomized, k=k)
        accuracies.append(accuracy)
    plot_accuracy(accuracies, iterations)


def get_int(label): # hanterar nummer-inmatning
    while True:
        try:
            value = input(f"{label}: ")
            return int(value)
        except ValueError:
            print("felaktig inmatning, ange siffror.")


def main_menu():
    choices = {
        1: "!- kör alla uppgifter enligt labb -!",
        2: "plotta klasser av datapunkter",
        3: "klassifiera test punkter mot data punkter, valfri K",
        4: "kalkylera minsta avstånd 0/50 av datapunkterna och kalkylera, specifiera K, plotta medelaccuracy",
        5: "ange egna värden för för klassifiering (uppgift 1)"
     }

    while True:
        for key, value in choices.items():
            print(f"{key}, {value}") 
        choice = get_int(label="Välj ditt val")
        if choice == 1:
            x = get_int(label="ange bredd(X)")
            y = get_int(label="ange Höjd(Y)")
            k = 10
            test_point = [x,y]
            print("\nuppgift 1")
            calc_distances(test_points=[test_point], test_point_classes=False)
            print("\nuppgift 2 (k=10, samma x,y värden)")
            calc_distances(test_points=[test_point], test_point_classes=False, k=k)
            input("\nEnter för nästa uppgift (slumpa data och fördela, räkna ut och plotta average)")
            scramble_dataset()
        elif choice == 2:
            print("laddar plot.")
            plot_tp_vs_dp()
        elif choice == 3:
            print(f"klassifierar {test_points}.. ange antal för K")
            k = get_int(label="k")
            calc_distances(k=k, test_point_classes=False)
        elif choice == 4:
            print(f"Slumpar en fördelning av data points.. \nAnge antal iterationer samt antal K:")
            iterations = get_int(label="iterationer")
            k = get_int(label="K")
            scramble_dataset(iterations=iterations, k=k)
        elif choice == 5:
            x = get_int(label="ange bredd(X)")
            y = get_int(label="ange Höjd(Y)")
            k = get_int(label="ange antal grannar")
            test_point = [x,y]
            print(test_point)
            calc_distances(test_points=[test_point], test_point_classes=False)

main_menu()

# txt_to_csv()
# plot_tp_vs_dp(csv_file)
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

#calc_distances(test_point_classes=False)


# 
# scramble_dataset(k=6, iterations=10)
# plot_accuracy()
# 

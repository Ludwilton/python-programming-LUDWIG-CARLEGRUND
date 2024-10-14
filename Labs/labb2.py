import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import os
import random as rng

# Debug prints shouldn't be in the final delivery
print(os.getcwd())

# this is a bit overly complicated. Since you are using pandas, just use pandas.read_csv with skipwors=1
with open("repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.txt", "r") as txt_file:
    lines = txt_file.readlines()
with open("repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.csv", "w") as csv_file:
    csv_write = csv.writer(csv_file)

    for line in lines[1:]:
        row = line.strip().split(", ")
        csv_write.writerow(row)
    
csv_file = "repos/python-programming-LUDWIG-CARLEGRUND/Labs/datapoints.csv"

with open(csv_file, "r") as data:
    lines = data.readlines()
data = []
for line in lines:
    row = line.strip().split(",")
    data.append(row)

# better to read these from the file
test_points = [
    [25, 32],
    [24.2, 31.5],
    [22, 34],
    [20.5, 34]
]

k = 1 # antal grannar knn_classifier kollar mot


def plot_tp_vs_dp(csv_file=csv_file): # plottar datapoints.csv
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


def calculate_distances(test_point, data): # returnerar avstånd mellan TP/DP samt klass för datapunkt
    distances = [(euc_distance(test_point[:2], data_point[:2]), data_point[2]) for data_point in data]
        # för att printa avstånd mellan varje test och datapunkt: 
        # # TODO gör så att detta funkar efter faktorering, låg prio, kan vara så att det inte går utan en loop i knn_classifier
        # for c, j in enumerate(distances):
        #     print(f"avstånd mellan TP:{i+1} och DP:{c+1} {j}")
    return distances


def get_k_nearest_neighbors(distances, k): # sorterar avstånd och returnerar en klasser för grannar i form av lista
    sorted_distances = sorted(distances, key=lambda x: x[0]) # passar vidare klassifiering 
    k_lowest = sorted_distances[:k] # lägger till K antal lägsta för varje test punkt
    return [neighbor[1] for neighbor in k_lowest]


def classify_point(k_neighbors, k): # klassifierar en punkt baserat på majoriteten av klass av grannpunkter
    '''
    note, round rundar neråt om lika många av varje, 
    om t.ex k=10 kan denna bli 0.5, en lösning till detta kan vara att ändra vikten av k per iteration.
    '''
    return round(sum(k_neighbors) / k)


def calculate_accuracy(tp, tn, fp, fn): # returnerar accuracy av klassifieraren
    return (tp + tn) / (tp + tn + fp + fn)

# Raphael says: Den här funktionen är lite väl komplex. Den har också sid-effekter som gör den svår att använda
# utanför detta skript (printar saker istället för att returnera dem). Returen är förvånansvärt accuracy och inte
# klassifikationen. 

# TODO testa så att omfaktoriseringen av denna är robust!! 1 -> 5 functions
def knn_classifier(test_points=test_points, data=data, k=k, plot_accuracy=True): # returnerar även accuracy om detta ska plottas

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    data = np.array(data, dtype=float)
    test_points = np.array(test_points, dtype=float)

    for c, test_point in enumerate(test_points):

        distances = calculate_distances(test_point, data)
        
        k_neighbors = get_k_nearest_neighbors(distances, k)

        predicted_class = classify_point(k_neighbors,k)
        
        if predicted_class == 1:
            print(f"Test punkt {c + 1} är av klassen Pikachu")
        else:
            print(f"Test punkt {c + 1} är av klassen Pichu")

        if plot_accuracy: # flaggan används när beräkning av medelaccuracy ska ske . # TODO flippa bool på flaggan lol
            # jämför predicted class mot test_points verkliga klasser -> rad[c] i test_points item = [2]
            if predicted_class == test_points[c, 2]:
                if predicted_class == 1:
                    tp += 1
                else:
                    tn += 1
            else:
                if predicted_class == 1:
                    fp += 1
                else:
                    fn += 1

    if plot_accuracy:
        return calculate_accuracy(tp, tn, fp, fn)
    

def plot_accuracy(accuracies, iterations):
    average_accuracy = sum(accuracies)/iterations
    print(f"medelaccuracy: {average_accuracy}") 
    plt.plot(accuracies, marker="o", linestyle="-", color="b", label="accuracy per iteration")
    plt.axhline(average_accuracy, label=f"Genomsnittlig accuracy ({average_accuracy*100:.2f}%)", linestyle="--")
    plt.title(f"Accuracy per iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid()
    plt.show()


# en mycket enklare lösning hade varit att köra np.random.shuffle(data) _innan_ du delar upp dem i pikachu/pichu

def scramble_dataset(data = data, k=k, iterations = 10): # delar slumpmässigt ut punkter till tp/dp med jämn fördelning av klasser.
    accuracies = []

    for _ in range(iterations):
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

        accuracy = knn_classifier(test_points_randomized, data_points_randomized, k=k)
        accuracies.append(accuracy)
    plot_accuracy(accuracies, iterations)


def get_int(label): # hanterar nummer-inmatning
    while True:
        try:
            value = input(f"{label}: ")
            return int(value)
        except ValueError:
            print("felaktig inmatning, ange siffror.")

# Meny baserade interface är väldigt klumpiga i text-form. Ett bättre val är argument till programmet (tex 'python3 labb2.py --plot' för alt 2 osv)
# Denna sortens indelning lämpar sig bättre för en jupyter notebook, där varje alternativ iställer är en cell.
def main_menu():
    choices = {
        1: "Kör alla uppgifter enligt labb - Börja här!",
        2: "Plotta klasser av datapunkter",
        3: "Klassifiera test punkter mot data punkter, valfri K",
        4: "Kalkylera minsta avstånd 0/50 av datapunkterna och kalkylera, specifiera K, plotta medelaccuracy",
        5: "Ange egna värden för klassifiering",
        6: "Avsluta programmet."
     }
    press_enter = "tryck enter för att gå vidare till menyn"
    while True:
        for key, value in choices.items():
            print(f"{key}, {value}") 
        choice = get_int(label="Välj ditt val")
        if choice == 1:
            x = get_int(label="Ange bredd(X)")
            y = get_int(label="Ange Höjd(Y)")
            k = 10
            test_point = [x,y]
            print("\nUppgift 1")
            knn_classifier(test_points=[test_point], plot_accuracy=False)
            print("\nUppgift 2 (k=10, samma x,y värden)")
            knn_classifier(test_points=[test_point], plot_accuracy=False, k=k)
            input("\nTryck enter för nästa uppgift: \n(slumpar data och fördelar 50x tp 100x dp, klassifierar, 10 iterations och plottar average accuracy)")
            scramble_dataset()
            input(press_enter)
        elif choice == 2:
            print("Visar scatterplot av datapoints.csv.")
            plot_tp_vs_dp()
            input(press_enter)
        elif choice == 3:
            print(f"Klassifierar {test_points}. Ange antal K")
            k = get_int(label="k")
            knn_classifier(k=k, plot_accuracy=False)
            input(press_enter)
        elif choice == 4:
            print(f"Slumpar en fördelning av data points.. \nAnge antal iterationer samt antal K:")
            iterations = get_int(label="iterationer")
            k = get_int(label="K")
            scramble_dataset(iterations=iterations, k=k)
            input(press_enter)
        elif choice == 5:
            x = get_int(label="Ange bredd(X)")
            y = get_int(label="Ange Höjd(Y)")
            k = get_int(label="Ange antal grannar")
            test_point = [x,y]
            print(test_point)
            knn_classifier(test_points=[test_point], plot_accuracy=False)
            input(press_enter)
        elif choice == 6:
            exit()

main_menu()

# txt_to_csv()
# plot_tp_vs_dp(csv_file)
# main_menu()

# knn_classifier([[10.5, 20],[18, 23], [30, 32], [10, 20], [12.5, 50]],[[19.332572350434354,32.25325633655492,0],
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

#knn_classifier(plot_accuracy=False)


# 
# scramble_dataset(k=6, iterations=10)
# plot_accuracy()
# 

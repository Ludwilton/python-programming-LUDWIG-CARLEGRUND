words_path = "/Users/luddecmc/Desktop/SKOLARBETE-ITHS/repos/python-programming-LUDWIG-CARLEGRUND/Other/Intro-AI-Rapport.md"

with open(words_path, "r") as file:
    word_count = file.read()
    number_of_words = []
    word_count = word_count.split(" ")
    for word in word_count:
        number_of_words.append(word)
    print(len(number_of_words))
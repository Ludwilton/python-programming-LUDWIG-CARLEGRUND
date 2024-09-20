# Uppgift - Arbetsflöde för AI-projekt
---

Ett projekt där maskininlärning eller djupinlärning är inblandat kräver oftast ett visst
antal steg i arbetsflödet.

Syftet med den här uppgiften är att få en teoretisk överblick
över de vanliga stegen i arbetsflödet av en maskininlärningsapplikation.

I den här uppgiften ska du teoretiskt beskriva dessa steg för ett scenario med maskininlärningsalgoritmen linjär regression.

Scenariot är att förutspå huspriser baserat på
olika ”features” såsom antalet rum, geografiska läget, storlek på huset med mera.

--- 

**Krav**
- skriva en rapport på 500-1000 ord.
- källhänvisa till samtliga källor du använt.
- beskriv hur man kan göra för att samla in datan, vilka format, vart kan man spara
datan?
- beskriv hur man kan visualisera datan?
- beskriv hur man kan göra för att bearbeta datan till rätt format?
- beskriv hur linjär regression fungerar.
- beskriv hur man kan göra för att driftsätta modellen?
- vilka teknologier kan man använda i de olika stegen i maskininlärningsprocessen?



---
## Förutspå huspriser med ML - ett arbetsflöde

#### linjär regression

linear regression is a supervised machine learning algorithm which is used to learn and make predictions on data. The algorithm models the relationship between one or several variables, in our case its the relationship between house pricing and several features, such as house size, number of room, location etc. Linear regression is one of the most well known and used algorithms in ML because of it's simplicity and the time it takes to train. 

#### datainsamling
the first and maybe the most important step to a good machine learning model is gathering high quality data, this can be done through a number of ways. a few examples include public databases such as the swedish scb(statistiska centralbyrån), or huggingface. in our example another solution would be to webscrape websites such as hemnet, booli, blocketbostad etc. or using a private dataset.

after gathering data it's important to structure in a table format with a column for each variable, which then is either saved into a csv file or put into a database such as sql

#### databearbetning

the collected data is usually raw, before we can use it in a model we need to process and prepare it. this includes handling missing data points, which can either be filled with a median or deleting.
Categorized variables such as for e.g location need to be converted into a numerical format. 
Because linear regression uses euclidean distance calculations, which is sensitive to the scale of variables, it's also helpful to scale the data so that no single variable dominates the distance calculations, this is often done by techniques such as standardization, normalization, or min-max scaling.


#### datavisualisering

before training your model it's good practice to visualize your data to understand the relationship between variables. It can also aid in recognizing patterns and deviations that are important for the model

this is usually done using the matplotlib or seaborn modules in python
an example would be using a scatterplot to visualize the relationship between house size and price.

![house price vs. size](price_size_relationshipgraph.png) [picture taken from w3schools](https://www.w3schools.com/ai/ai_regressions.asp)


#### driftsättning

#### olika teknologier

one-hot encoding

#### källor
[w3schools](https://www.w3schools.com/ai/ai_regressions.asp)
[geeksforgeeks](https://www.geeksforgeeks.org/ml-linear-regression/#what-is-linear-regression)
[machinelearningmastery.com](https://machinelearningmastery.com/linear-regression-for-machine-learning/)
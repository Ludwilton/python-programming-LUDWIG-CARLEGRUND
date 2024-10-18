# klassifiering och visualisering av datapunkter med labb3.py

---

### Sammanfattning

Detta program klassificerar datapunkter med en linjär separationslinje, och visualiserar resultaten i ett spridningsdiagram med möjlighet att visualisera flera linjer samtidigt. Programmet kan också spara de klassificerade punkterna till en CSV-fil. 


#### get_data()
med denna funktion läses "unlabelled_data.csv" in, denna fil måste ligga i samma direktiv som script-filen.

 denna data konverteras sedan om till en numpy-array och returneras i detta format.
 
 Varje funktion i programmet som använder datan, använder också funktionen get_data(), men det är går även att överlagra denna data med egna värden.

denna datan måste då innehålla punkter i form av x och y kordinater i form av float värden i en array.

#### classify_data_points()
denna funktion använder get_data() och genomför en klassifikation med en linjär separationslinje, användaren kan mata in egna värden för lutning och skärningspunkt, om dessa inte matas in använder programmet sig automatiskt av default-värdena (k=0.5, M=0). funktionen returnerar en lista av originaldatan med en klassifikations-label i den tredje kolumnen, detta är antingen 0 eller 1 beroende på vilken sida av separationslinjen datapunkten ligger av.

denna klassifieringsfunktion används av plot_classified_points och write_classified labels. dessa kan båda ta in k och m som parametrar för att passa vidare till klassifieraren.

#### plot_classified_points
denna funktion tar parametrarna: k, m, axes, color, label.
 om dessa inte anges använder funktionen sig av default-värden.

funktionen använder sig av classify_data_points för att och visualiserar sedan den returnerade datan i ett spridningsdiagram

blå punkt representerar höger om seperationslinje och gul för för vänster om. Diagrammet visar även separationslinjen som använts för att klassifiera punkterna.

#### write_classified_data_csv
denna funktion kallar på classify_data_points och skriver den returnerade datan till "labelled_data.csv" under samma direktiv som scriptet körs i.



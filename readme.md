# Outils de secrétaire
Ce programme a pour but de faciliter la création de divers documents pour la société, il faut cependant fournir quelques documents au préalable.
Ces documents doivent être placée dans le dossier template, ou data.

# Entrée
- X documents voulus, sous format markdown dans le dossier template. Vous pouvez également ajouter des éléments htmls
dans ce markdown qui seront pris en compte lors de la créations en pdf. La liste des variables constant sont située dans le dossier
data dans le fichier valConst.csv. Veuillez respect le format {{Variable}} pour que le programme remplissent automatiquement les champs

- Un fichier valConst.csv située dans le dossier data. Vous pouvez modifier ce dossier pour ajouter des nouvelles variables ou changer
les existants. Ce fichier peut être ouvert en excel, veuillez cependant respecter le format imposé (Trois cellules). Certains valeurs
ne sont pas affichée dans ce fichier car ils sont calculé automatiquement
- - ANNEE : L'année actuels
- - NB_PRESENT : Le nombre de membre présent durant l'assemblée générale
- - ANNEE_PRECEDENT : L'année précédent
- - TRAINING / OPEN_DOORS / CAMPAIGN / ENDING_SHOOT Correspond au date de certains événements. Elles se remplissent automatiquement lors de la création du faire-part

- Un pdf contenant les dates des jours de tirs. Un pdf d'exemple existe dans le dossier data (qui doit contenir votre nouveau planning)
- Un fichier csv contenant les informations pour les rappels. Merci de suivre le format de date (Année-Mois-Jour)

# Programming
Cette partie doit être complèter pour contenir des éléments devant être modifié depuis le code
- md_generator
- - data_tableau est un tableau utilisé pour la fonction membres uniquement. Elle permet de définir les champs que votre tableau doit contenir

# Utilisaton
Lorsque le programme démarre, vous aurez une liste de choix: Crée un/des mds à partir de templates et les exporter en pdf, Créer un fichier contenant les dates des séances de tirs, Effectuer les deux commandes précédentes ou encore exporter un/des markdowns en pdf. Cette dernière fonction est utilisé si vous avez modifier quelques lignes directements sur les markdowns situées dans le dossier de l'année.

# Sortie 
Le programme crée un dossier correspondant à l'année actuel, avec ( en assumant que vous avez choisi l'option de tout exécuté), un fichier pdf et markdown
par template, complèter par les valeurs contenues dans valConst. Vous aurez aussis un fichier .ics contenant les dates des séances de tir que vous pourrez
importer dans un calendrier comme google calendar
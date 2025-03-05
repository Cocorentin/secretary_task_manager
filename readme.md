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

- Un pdf contenant les dates des jours de tirs. Un pdf d'exemple existe dans le dossier data (qui doit contenir votre nouveau planning)

# Utilisaton
Lorsque le programme démarre, vous aurez le choix en fonction des valeurs insèré. Si vous n'avez pas fournit de template, vous ne pourrez
seuleument que export les dates des jours de tirs. Ces dates pourront ensuite être ajoutée à votre google calendar. Si des templates ont été fournis,
vous aurez une option pour créer chacunes séparément, ou toutes en même temps. Vous aurez par ailleurs l'option de créer tout les documents en plus d'exporter
les dates. A SUPPRIMER Actuellement il faut rajouter un check s'il n'y a pas de planning

# Sortie 
Le programme crée un dossier correspondant à l'année actuel, avec ( en assumant que vous avez choisi l'option de tout exécuté), un fichier pdf et markdown
par template, complèter par les valeurs contenues dans valConst. Vous aurez aussis un fichier .ics contenant les dates des séances de tir que vous pourrez
importer dans un calendrier comme google calendar
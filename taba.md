# TO BE DONE
- **Si un fichier est déjà crée ne pas l'écraser :D**
- Export des dates + type de tir au format **ics**
- générateur python basé sur des templates MD + placeholders fichier csv pour valeur fix
  - SI POSSIBLE, un fichier qui contient mes vars... à modifier
  - Convocation AG |
  - Feuille PV |
  - Faire part pour Laconnex
  - Feuille des membres avec info perso |
  - Comité |

## Pas obligatoire mais très très cool même pour toi
- OCR sur les dates de tir fichier pdf
- ++ me créer les fichiers MD + les PDF directements
- +++ packager application puis contenairisé -> dockerfile
- ++++ Interface web flask génère le csv






# Chemins des fichiers
TEMPLATE_PATH = os.path.join("./template", "convocation_ag.md")
OUTPUT_FILENAME = f"{ANNEE}_AG.md"
OUTPUT_PATH = os.path.join("./", OUTPUT_FILENAME)


# Somewhat
- Truc dynamique qui me permet de créer des tâches dans mon agenda **ics** (Remplacer les task par des événement)
- - Les tâches ne sont malheureusement pas importable dans le calendrier
- - Google task n'importe pas les tâches

# Done
- Créer un répertoire de l'année en cours

class Menu
Class Md/Pdf
Class ISC


1 Get Calender ISC
2 Get All MD/PDF
3 Get Convocation 
4 Get Pv
5 Get FairPart
6 Get Member
7 Get ALL
8 Exit

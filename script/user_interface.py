import os
import sys
from datetime import datetime
from script.md_generator import md_generator
from script.calendar_event import calendar_event


class user_interface:
        
    def __init__(self):
        try:
            self.md_tools = md_generator()
            self.isc_tools = calendar_event()
            self.annee_actuelle = datetime.now().year
        except:
            print("ERROR: Un/Des scripts ont été bougée du dossier script, ou le dossier a été déplacé ailleur que dans le dossier courant. Assurez vous que md_generator.py et calendar_event sont dans le même répertoire que user_interface")
            sys.exit()
            
                
    def _gen_all_md(self):    
        self.md_tools.gen_md("convocation_ag")
        self.md_tools.gen_fp_md("faire_part")
        self.md_tools.gen_member_md("membres")
        self.md_tools.gen_md("pv_ag")
            
    def _gen_all_pdf(self):    
        """
        Exporter tout les mds présent dans le dossier de l'année actuel en pdf. Cette fonction ne plante pas s'il n'y a pas tout les mds présents.
        """
        for file in  os.listdir(f"./{datetime.now().year}"):
            if file.endswith(".md"):
                self.md_tools.md_to_pdf(file[:-3])
        
        
    def _menu_md(self):
        """
        Affiche le menu pour convertir les templates en markdowns remplis
        """
        option_md = "0 Créer la convocation\n1 Crée le fair part\n2 Créer les membres\n3 Crée le pv\n4 Tout créer\nExit pour returner au menu précédent\n"
        while True:
            print(option_md)
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self.md_tools.gen_md("convocation_ag")
                case "1":
                    self.md_tools.gen_fp_md("faire_part")
                case "2":
                    self.md_tools.gen_member_md("membres")
                case "3":
                    self.md_tools.gen_md("pv_ag")
                case "4":
                    self._gen_all_md()                                        
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer une commande valide\n")

    
    def _menu_pdf(self):
        """
        Retourne un menu permettant l'exportation de un/tout le(s) fichiers md stocké dans le dossier de l'année actuel. Cet fonction
        ne vérifie pas si le fichier voulu existe.
        """             
        option_pdf = "0 Exporter la convocation\n1 Exporter le fair part\n2 Exporter les membres\n3 Exporter le pv\n4 Tout exporter\nExit pour returner au menu précédent\n"
        while True:
            print(option_pdf)
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self.md_tools.md_to_pdf(f"convocation_ag_{self.annee_actuelle}")
                case "1":
                    self.md_tools.md_to_pdf(f"faire_part_{self.annee_actuelle}")
                case "2":
                    self.md_tools.md_to_pdf(f"membres_{self.annee_actuelle}")
                case "3":
                    self.md_tools.md_to_pdf(f"pv_ag_{self.annee_actuelle}")
                case "4":
                    self._gen_all_pdf()
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer une commande valide\n")
            
    def run(self):
        """
        lst_file is a list containing all the filename in the template folder
        This function let you start the interace, allowing the user to have the
        programm executed the task needed
        """
        option_lst = "0 Créer MD\n1 Créer ICS\n2 Créer ALL\n3 Export PDF\nExit pour quitter le programme"
        
        while True:
            print(option_lst)
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self._menu_md()
                case "1":
                    self.isc_tools.export_to_calendar()
                case "2":
                    event_date = self.isc_tools.export_to_calendar()
                    self._gen_all_md()
                case "3":
                    self._menu_pdf()
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer un chiffre correspondant à une des actions autorisées \n")

                

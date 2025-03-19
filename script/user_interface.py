import os
import sys
from datetime import datetime
from script.md_generator import md_generator
from script.calendar_event import calendar_event
from simple_term_menu import TerminalMenu



class user_interface:
        
    def __init__(self):
        try:
            self.md_tools = md_generator()
        except Exception as e:
            print(f"{e}")
            sys.exit()
        try:
            self.isc_tools = calendar_event()
        except Exception as e:
            print(f"{e}")
            sys.exit()
        self.annee_actuelle = datetime.now().year
            
                
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

        lst_available_pdf = []
        for file in  os.listdir(f"./{datetime.now().year}"):
            if file.endswith(".md"):
                lst_available_pdf.append(file[:-3])
                
                
        if len(lst_available_pdf) == 0:
            print("Vous n'avez pas de fichier md exportable, veuillez les crée d'abords.")
            return None
    
        option_pdf = []
        for file in lst_available_pdf:
            option_pdf.append(f"{file}")
                        
        option_pdf.append(f"Retourner au menu précèdent")
        terminal_menu = TerminalMenu(option_pdf,
                                     title="Exporter un fichier en pdf",
                                     multi_select=True,
                                     show_multi_select_hint=True,)
        while True:
            menu_entry_index = terminal_menu.show()
            for select_opt in terminal_menu.chosen_menu_entries:
                if select_opt.startswith("Retourner"):
                    return None
                else:
                    self.md_tools.md_to_pdf(select_opt)
            
    def _menu_ics(self):
        """
        Affiche le menu pour convertir les csv en fichier ics pour exporter dans google calendar
        """
        option_md = "0 Exporter les dates de tirs\n1 Export les rappels\n2 Tout exporter\nExit pour returner au menu précédent\n"
        while True:
            print(option_md)
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self.isc_tools.export_to_calendar()
                case "1":
                    self.isc_tools.export_reminder()
                case "2":
                    self.isc_tools.export_to_calendar()
                    self.isc_tools.export_reminder()                    
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
                    self._menu_ics()
                case "2":
                    event_date = self.isc_tools.export_to_calendar()
                    self._gen_all_md()
                case "3":
                    self._menu_pdf()
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer un chiffre correspondant à une des actions autorisées \n")

                

import os
import sys
from datetime import datetime
import pathlib
#from pdfquery import PDFQuery
from ics import Calendar, Event, Todo
from datetime import datetime
import time
#Extract Data into array here
from pypdf import PdfReader
import re
import pandas as pd
from markdown_pdf import MarkdownPdf,Section
from script.md_generator import md_generator
from script.calendar_event import calendar_event


class user_interface:
        
    def __init__(self):
        try:
            self.lst_extentless = []
            lstFile = os.listdir("./template")
            for file in lstFile:
                self.lst_extentless.append(file[:-3])
        except:
            print("ERROR: Le dossier template a été bougé ou n'existe pas, cela ne devrait pas arrivé si vous avez seuleument déplacé les templates dedans.")
            sys.exit()
            
    def _dyn_available_action(self,lst_size : int):
        command_panel = "Veuiller entrer le nombre correspondant à l'action attendu. Tout autre actions ne correspondant pas au choix offert arrêtera l'application \n"
        if lst_size == 0:
            command_panel += "0 Exporter les dates pour google calendar\n"
        else:
            self.cmpt = 0
            for filename in self.lst_extentless:
                command_panel += f"{self.cmpt} Créer {filename}\n"
                self.cmpt += 1
            command_panel += f"{self.cmpt} Créer les documents seulement\n{self.cmpt+1} Exporter les dates pour google calendar\n{self.cmpt+2} Tout exécuter\n"
        print(command_panel)
        
    def _menu_md(self):
        for idx in range(len(self.lst_extentless)):
            print(f"OwO, do you want to print {self.lst_extentless[idx]}? Pwess {idx}")    
        print("Pwess 2 for all\nPwess exit to go back to the main menu")
        md_tools = md_generator()
        while True:
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    md_tools.gen_mdfile(self.lst_extentless[0])
                case "1":
                    md_tools.gen_mdfile(self.lst_extentless[1])
                case "2":
                    for file in self.lst_extentless:
                        md_tools.gen_mdfile(file)
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer un chiffre correspondant à une des actions autorisées \n")
            #else:
                #break
                 
            
            
    def run(self):
        """
        lst_file is a list containing all the filename in the template folder
        This function let you start the interace, allowing the user to have the
        programm executed the task needed
        """
        isc_tools = calendar_event()
        lst_size = len(self.lst_extentless)
        
        #self._dyn_available_action(lst_size)
        print("0 Créer MD\n1 Créer ICS\n2 Créer ALL\n3 exit")
        
        while True:
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self._menu_md()
                    print("0 Créer MD\n1 Créer ICS\n2 Créer ALL\n3 exit")
                case "1":
                    isc_tools.export_to_calendar()
                case "2":
                    event_date = isc_tools.export_to_calendar()
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer un chiffre correspondant à une des actions autorisées \n")
            #else:
                #break
                
        
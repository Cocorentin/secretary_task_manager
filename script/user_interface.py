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
            self.md_tools = md_generator()
            self.lst_extentless = []
            lstFile = os.listdir("./template")
            for file in lstFile:
                self.lst_extentless.append(file[:-3])
            self.lst_extentless = sorted(self.lst_extentless)
        except:
            print("ERROR: Le dossier template a été bougé ou n'existe pas, cela ne devrait pas arrivé si vous avez seuleument déplacé les templates dedans.")
            sys.exit()
            
                
    def _gen_all_md(self):    
        self.md_tools.gen_mdfile("convocation_ag")
        self.md_tools.gen_fp_md("faire_part")
        self.md_tools.gen_member_md()
        self.md_tools.gen_mdfile("pv_ag")
            
    def _gen_all_pdf(self):    
        for file in self.lst_extentless:
            self.md_tools.md_to_pdf(file)
        
        
    def _menu_md(self):
        option_md = "0 Créer la convocation\n1 Crée le fair part\n2 Créer les membres\n3 Crée le pv\n4 Tout créer\nExit pour returner au menu précédent"
        while True:
            print(option_md)
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self.md_tools.gen_mdfile("convocation_ag")
                case "1":
                    self.md_tools.gen_fp_md("faire_part")
                case "2":
                    self.md_tools.gen_member_md()
                case "3":
                    self.md_tools.gen_mdfile("pv_ag")
                case "4":
                    self._gen_all_md()                                        
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer une commande valide\n")
            #else:
                #break
    
    def _menu_pdf(self):             
        option_pdf = "0 Exporter la convocation\n1 Exporter le fair part\n2 Exporter les membres\n3 Exporter le pv\n4 Tout exporter\nExit pour returner au menu précédent"
        while True:
            print(option_pdf)
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self.md_tools.md_to_pdf("convocation_ag")
                case "1":
                    self.md_tools.md_to_pdf("faire_part")
                case "2":
                    self.md_tools.md_to_pdf("membres")
                case "3":
                    self.md_tools.md_to_pdf("pv_ag")
                case "4":
                    self._gen_all_pdf
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
        isc_tools = calendar_event()
        lst_size = len(self.lst_extentless)
        option_lst = "0 Créer MD\n1 Créer ICS\n2 Créer ALL\n3 Export PDF\nExit pour quitter le programme"
        
        while True:
            print(option_lst)
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self._menu_md()
                    print("0 Créer MD\n1 Créer ICS\n2 Créer ALL\n3 exit")
                case "1":
                    isc_tools.export_to_calendar()
                case "2":
                    event_date = isc_tools.export_to_calendar()
                    self._gen_all_md()
                case "3":
                    self._menu_pdf()
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer un chiffre correspondant à une des actions autorisées \n")
            #else:
                #break
                

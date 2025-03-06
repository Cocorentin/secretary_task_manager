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
        except:
            print("ERROR: Le dossier template a été bougé ou n'existe pas, cela ne devrait pas arrivé si vous avez seuleument déplacé les templates dedans.")
            sys.exit()
            
        
    def _gen_all_md(self):    
        for file in self.lst_extentless:
            self.md_tools.gen_mdfile(file)
        
        
    def _menu_md(self):
        option_md = ""
        for idx in range(len(self.lst_extentless)):
            option_md += f"OwO, do you want to print {self.lst_extentless[idx]}? Pwess {idx}\n"
        option_md += "Pwess 2 for all\nPwess exit to go back to the main menu"
        print(option_md)
        while True:
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self.md_tools.gen_mdfile(self.lst_extentless[0])
                case "1":
                    self.md_tools.gen_mdfile(self.lst_extentless[1])
                case "2":
                    self._gen_all_md()
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer un chiffre correspondant à une des actions autorisées \n")
                    print(option_md)
            #else:
                #break
    
    def _menu_pdf(self):             
        option_pdf = "Please select one of the number to export the following md"
        for idx in range(len(self.lst_extentless)):
            option_md += f"{self.lst_extentless[idx]}? Pwess {idx}\n"
        print(option_md)
        while True:
            answ = input("Entrer l'action souhaité : ")
            match answ.lower():
                case "0":
                    self.md_tools.gen_mdfile(self.lst_extentless[0])
                case "1":
                    self.md_tools.gen_mdfile(self.lst_extentless[1])
                case "2":
                    self._gen_all_md()
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer un chiffre correspondant à une des actions autorisées \n")
                    print(option_md)            
            
    def run(self):
        """
        lst_file is a list containing all the filename in the template folder
        This function let you start the interace, allowing the user to have the
        programm executed the task needed
        """
        isc_tools = calendar_event()
        lst_size = len(self.lst_extentless)
        option_lst = "0 Créer MD\n1 Créer ICS\n2 Créer ALL\n3 exit"
        print(option_lst)
        
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
                    self._gen_all_md()
                case "exit":
                    break
                case "" | _:
                    print("Veuillez entrer un chiffre correspondant à une des actions autorisées \n")
                    print(option_lst)
            #else:
                #break
                
        
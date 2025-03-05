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
            cmpt = 0
            for filename in self.lst_extentless:
                command_panel += f"{cmpt} Créer {filename}\n"
                cmpt += 1
            command_panel += f"{cmpt} Créer les documents seulement\n{cmpt+1} Exporter les dates pour google calendar\n{cmpt+2} Tout exécuter\n"
        print(command_panel)
        
    
    def run(self):
        """
        lst_file is a list containing all the filename in the template folder
        This function let you start the interace, allowing the user to have the
        programm executed the task needed
        """
        md_tools = md_generator()
        isc_tools = calendar_event()
        lst_size = len(self.lst_extentless)
        
        self._dyn_available_action(lst_size)
        
        while True:
            answ = input("Entrer l'action souhaité : ")
            if answ.isdigit():
                answ_int = int(answ)
                if lst_size != 0:
                    if answ_int == lst_size:
                        for file in self.lst_extentless:
                            md_tools.gen_mdfile(file)
                    elif answ_int < lst_size:
                        md_tools.gen_mdfile(self.lst_extentless[answ_int])
                    elif answ_int == cmpt+1:
                        res = isc_tools.export_to_calendar()
                    elif answ_int == cmpt+2:
                        res = isc_tools.export_to_calendar()
                        for file in self.lst_extentless:
                            md_tools.gen_mdfile(file)
                    else :
                        break
                else:
                    if answ_int == 0:
                        isc_tools.export_to_calendar()
                    else:
                        break
            else:
                break
            print("Action effectuée")    
                
        
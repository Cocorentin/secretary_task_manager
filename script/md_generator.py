import os
import sys
from datetime import datetime
import pathlib
#from pdfquery import PDFQuery
from ics import Calendar, Event, Todo
import calendar
from datetime import datetime
import time
#Extract Data into array here
from pypdf import PdfReader
import re
import pandas as pd
from markdown_pdf import MarkdownPdf,Section
from script.calendar_event import calendar_event
import locale


class md_generator:
    def __init__(self):
        locale.setlocale(category=locale.LC_ALL,locale="fr_FR.utf8")
        val_indisponible = "LA VALEUR EST MANQUANT DANS LES DATES DE TIRS"
        self.data_tableau = ["Role","Nom Prenom"]
        try:
            self.df = pd.read_csv('./data/valConst.csv',sep=";",index_col=0)
            self.nbMembre = len(self.df.loc["PRESENT_MEMBERS"]["Information"].split(','))
        except:
            print("ERROR : Le fichier de données n'est pas au bon endroit ou son nom a été modifié. Cela ne devrait pas arriver si vous n'avez modifié que le contenue de valConst.csv avec excel ou à la main (mais dans ce cas la, je suis sur que Coco ne verra pas sa)")
            sys.exit()
        self.annee_actuelle = datetime.now().year
        self.lstACalc = {"ANNEE" : str(self.annee_actuelle), "NB_PRESENT" : str(self.nbMembre), "ANNEE_PRECEDENT" : str(self.annee_actuelle-1),"TRAINING" : val_indisponible, "OPEN_DOORS" : val_indisponible, "CAMPAIGN":val_indisponible, "ENDING_SHOOT":val_indisponible}
        self.PATH_RES_FOLDER = sys.path[0] + "/" + str(self.annee_actuelle)
        pathlib.Path(self.PATH_RES_FOLDER).mkdir(exist_ok=True)


    def _get_lst_dynvar(self,pattern_needed : str,text_to_match: str):
        """
        Renvoie une list contenant tout les variables uniques nécessitant
        d'être completé
        """
        pattern_row_data = re.compile(pattern_needed)
        res = pattern_row_data.findall(text_to_match)
        return list(dict.fromkeys(res))
    
    def sanitize_word(self,word):
    #Remove '{{' and '}}' from the given word.
        return re.sub(r'{{(.*?)}}', r'\1', word)    
        
    def gen_mdfile(self,filename : str):
        """ 
        Permet la création du markdown et du pdf du template avec les valeurs constante remplacé par celle attendu. 
        :param str filename: Le nom du fichier template (sans l'extension) à remplir et exporter en pdf
        """    
        
        try:
            f = open(f'template/{filename}.md', 'r') 
        except:
            print(f"Erreur, vous n'avez pas mis le template {filename}.md dans le dossier template.")
            exit()
        md_content = f.read() 
        removed_secondentry = self._get_lst_dynvar("\{[^}]*\}}",md_content)
        
        for entry_to_change in removed_secondentry:
            cleaned_index = self.sanitize_word(entry_to_change)
            if cleaned_index in self.lstACalc :
                md_content = md_content.replace(entry_to_change,self.lstACalc[cleaned_index])
            else :
                md_content = md_content.replace(entry_to_change,self.df.loc[cleaned_index]["Information"])
        t = open(f'{self.PATH_RES_FOLDER}/{filename}_{self.annee_actuelle}.md', 'w') 
        t.write(md_content)
        t.close()
        self.md_to_pdf(f"{filename}")
        print(f"Le fichier {filename}.md a été crée et importé en pdf avec succès")
        
        
        
    def gen_member_md(self):
        try:
            f = open(f'template/membres.md', 'r') 
        except:
            print(f"Erreur, vous avez supprimé/déplacé le template membres.md du dossier template.")
            exit()
        try:
            dm = pd.read_csv(f'./data/membres.csv',sep=";") 
        except:
            print(f"Erreur, vous avez supprimé/déplacé le fichier membres.csv du dossier data.")
            exit()
        
        md_content = f.read()
        removed_secondentry = self._get_lst_dynvar("\{[^}]*\}}",md_content)
        for entry_to_change in removed_secondentry:
            cleaned_index = self.sanitize_word(entry_to_change)
            if cleaned_index in self.lstACalc :
                md_content = md_content.replace(entry_to_change,self.lstACalc[cleaned_index])
            #Cela indique que on a un tableau
            elif 'TABLE' in cleaned_index :
                #Remplacer par création du tableau html + par défaut Role | Nom Prénom
                array_html = "<table><tr>"
                for header in self.data_tableau:
                    array_html += f"<th>{header}</th>"
                array_html += "</tr>"
                lst_entry = cleaned_index.split(sep='|')
                for idx in range(len(dm)):
                    array_html += self.get_row_table(idx,dm)
                array_html += "</table>"
                md_content = md_content.replace(entry_to_change,array_html)                
            else :
                md_content = md_content.replace(entry_to_change,self.df.loc[cleaned_index]["Information"])
        t = open(f'{self.PATH_RES_FOLDER}/membres_{self.annee_actuelle}.md', 'w') 
        t.write(md_content)
        t.close()
        self.md_to_pdf(f"membres")
        print("Le fichier membre a été crée et importé avec succès")
            
    def get_row_table(self,index:int,df_membre):
        row = "<tr>"
        for val in self.data_tableau:
            if len(val.split(' ')) > 1:
                row += "<td>"
                for concat_val in val.split(' '):
                    row += df_membre.loc[index][concat_val] + " "     
                row += "</td>"
            else :
                row += "<td>" + df_membre.loc[index][val] + "</td>"
        return row + "</tr>"
                
            
    def md_to_pdf(self,filename: str):
        """
        Permet d'exporter un markdown en pdf, le markdown peut contenir des éléments htmls qui seront pris
        en compte lors de la conversion.
        :param str filename: Le nom du fichier md qui doit être exporter
        """
        fMd = open(f'{self.PATH_RES_FOLDER}/{filename}_{self.annee_actuelle}.md', 'r')
        md_content = fMd.read()
        fMd.close()
        pdf = MarkdownPdf(toc_level=2)
        pdf.add_section(Section(md_content))
        pdf.save(f"{self.PATH_RES_FOLDER}/{filename}.pdf")
        
    def FAIR_PART_FUNC(self,filename:str):
        isc_tools = calendar_event()
        lst_event = isc_tools.get_lst_date()
                    
        try:
            f = open(f'template/{filename}.md', 'r') 
        except:
            print(f"Erreur, vous n'avez pas mis le template {filename}.md dans le dossier template.")
            exit()
            
        lst_OP = dict()
        
        for x in lst_event :
            match x[4]:
                case "Autres" :
                    if x[5] == "Tir":
                        self.lstACalc["ENDING_SHOOT"] = x[0]
                    else:
                        self.lstACalc["OPEN_DOORS"] = x[0]
                case "TR":
                    self.lstACalc["TRAINING"] = x[0]
                case "FS":
                    self.lstACalc["CAMPAIGN"] = x[0]
                case _:
                    jour_semaine = datetime.strptime(x[0], "%d.%m.%Y").strftime("%A")
                    elem_date = x[0].split('.')
                    mois = calendar.month_name[int(elem_date[1])]
                    lst_OP["Tmp"].append(f"{elem_date[0]}")

        
        md_content = f.read() 
        removed_secondentry = self._get_lst_dynvar("\{[^}]*\}}",md_content)
        
        for entry_to_change in removed_secondentry:
            cleaned_index = self.sanitize_word(entry_to_change)
            if cleaned_index in self.lstACalc :
                md_content = md_content.replace(entry_to_change,self.lstACalc[cleaned_index])
            else :
                md_content = md_content.replace(entry_to_change,self.df.loc[cleaned_index]["Information"])
        t = open(f'{self.PATH_RES_FOLDER}/{filename}_{self.annee_actuelle}.md', 'w') 
        t.write(md_content)
        t.close()
        self.md_to_pdf(f"{filename}")
        print("tmp")
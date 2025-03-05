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

class md_generator:
    def __init__(self):
        try:
            self.df = pd.read_csv('./data/valConst.csv',sep=";",index_col=0)
            self.nbMembre = len(self.df.loc["PRESENT_MEMBERS"][0].split(','))
        except:
            print("ERROR : Le fichier de données n'est pas au bon endroit ou son nom a été modifié. Cela ne devrait pas arriver si vous n'avez modifié que le contenue de valConst.csv avec excel ou à la main (mais dans ce cas la, je suis sur que Coco ne verra pas sa)")
            sys.exit()
        self.annee_actuelle = datetime.now().year
        self.lstACalc = {"ANNEE" : str(self.annee_actuelle), "NB_PRESENT" : str(self.nbMembre), "ANNEE_PRECEDENT" : str(self.annee_actuelle-1)}
        self.PATH_RES_FOLDER = sys.path[0] + "/" + str(self.annee_actuelle)
        pathlib.Path(self.PATH_RES_FOLDER).mkdir(exist_ok=True)

    
    def get_template_name(self) -> []:
        """
        Renvoie une liste contenant tout les noms des fichiers sans
        leurs extensions contenues dans le dossier templates.
        """
        return self.lstExtentless.copy()

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

        f = open(f'template/{filename}.md', 'r') 
        md_content = f.read() 
        removed_secondentry = self._get_lst_dynvar("\{[^}]*\}}",md_content)
        
        for entry_to_change in removed_secondentry:
            cleaned_index = self.sanitize_word(entry_to_change)
            if cleaned_index in self.lstACalc :
                md_content = md_content.replace(entry_to_change,self.lstACalc[cleaned_index])
            else :
                md_content = md_content.replace(entry_to_change,self.df.loc[cleaned_index][0])
        t = open(f'{self.PATH_RES_FOLDER}/{filename}_{self.annee_actuelle}.md', 'w') 
        t.write(md_content)
        t.close()
        self._md_to_pdf(md_content,filename)
            
    def _md_to_pdf(self,text_md: str,filename: str):
        pdf = MarkdownPdf(toc_level=2)
        pdf.add_section(Section(text_md))
        pdf.save(f"{self.PATH_RES_FOLDER}/{filename}_{self.annee_actuelle}.pdf")
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
    PATH_RES_FOLDER = ""
    def __init__(self):
        try:
            self.df = pd.read_csv('./data/valConst.csv',sep=";",index_col=0)
            self.nbMembre = len(self.df.loc["PRESENT_MEMBERS"][0].split(','))

        except:
            print("ERROR : Le fichier de données n'est pas au bon endroit ou son nom a été modifié. Cela ne devrait pas arriver si vous n'avez modifié que le contenue de valConst.csv avec excel ou à la main (mais dans ce cas la, je suis sur que Coco ne verra pas sa)")
            sys.exit()
        try:
            self.lstExtentless = []
            lstFile = os.listdir("./template")
            for file in lstFile:
                self.lstExtentless.append(file[:-3])
        except:
            print("ERROR: Le dossier template a été bougé ou n'existe pas, cela ne devrait pas arrivé si vous avez seuleument déplacé les templates dedans.")
            sys.exit()
        self.annee_actuelle = datetime.now().year
        self.lstACalc = {"YEAR" : str(self.annee_actuelle), "NB_PRESENT" : str(self.nbMembre), "ANNEE_PRECEDENT" : str(self.annee_actuelle-1)}
        PATH_RES_FOLDER = sys.path[0] + "/" + str(self.annee_actuelle)
        pathlib.Path(PATH_RES_FOLDER).mkdir(exist_ok=True)

    
    def get_template_name(self) -> []:
        """
        Return a list containing all the template found in
        the folder template. The extension has been removed
        """
        return self.lstExtentless.copy()

    
    def gen_mdfile(self,filename : str):
        """ 
        Permet la création du markdown et du pdf du template avec les valeurs constante remplacé par celle attendu. 
        :param str filename: Le nom du fichier template (sans l'extension) à remplir et exporter en pdf
        """    

        f = open(f'template/{filename}.md', 'r') 
        md_content = f.read() 
        pattern_row_data = re.compile("\{[^}]*\}}")
        res = pattern_row_data.findall(md_content)
        removed_secondentry = list(dict.fromkeys(res)) 
        for x in removed_secondentry:
            cleaned_index = sanitize_word(x)
            if cleaned_index in lstACalc :
                md_content = md_content.replace(x,lstACalc[cleaned_index])
            else :
                md_content = md_content.replace(x,df.loc[cleaned_index][0])
        t = open(f'./{filename}_{annee_actuelle}.md', 'w') 
        t.write(md_content)
        t.close()
            
    def __md_to_pdf(self,text_md: str,filename: str):
        pdf = MarkdownPdf(toc_level=2)
        annee = current_year = datetime.now().year
        pdf.add_section(Section(text_md))
        pdf.save(f"{filename}_{annee}.pdf")
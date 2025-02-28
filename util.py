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

CUR_YEAR_PATH = sys.path[0] + "/" + str(datetime.now().year)

def get_ics_shooting():
    
    pdf = PDFQuery('example.pdf')
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal')

    # Extract the text from the elements
    text = [t.text for t in text_elements]

    print(text)    

def init_document():
    pathlib.Path(CUR_YEAR_PATH).mkdir(exist_ok=True)
    
    
def get_pdf_data(cur_page,lst_val):
    pattern_row_data = re.compile("^(\d{2}.\d{2}.\d{4}).*")

    for entry in cur_page:
        if pattern_row_data.match(entry):
            lst_val.append(entry.split(" "))
        
    
    
#Renvoi un ics avec des dates formater à UTC+2
def export_to_calendar():

    # creating a pdf reader object
    reader = PdfReader('2025/Annonce des jours de tirs_2025_03022025.pdf')

    # printing number of pages in pdf file
    #print(len(reader.pages))


    tmp = []
    
    #for each page, we extract the text and split into array before matching it
    for x in range(len(reader.pages)):
        page = reader.pages[x]
        raw_text = page.extract_text()
        split_txt = raw_text.splitlines()
        get_pdf_data(split_txt,tmp)
    
    
    #Create ISC
    delim = "-"
    c = Calendar()
    for entry in tmp:
        e = Event()
        ymd = entry[0].split(".")
        ymd[0], ymd[2] = ymd[2], ymd[0]
        date_event = delim.join(ymd)
        e.name = "Évenement de type " + entry[4]
        e.begin = datetime.fromisoformat(date_event +"T" + entry[1] +":00+02:00")
        e.end = datetime.fromisoformat(date_event +"T" + entry[2] + ":00+02:00")
        c.events.add(e)
    c.events
    # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
    with open( CUR_YEAR_PATH +'/Date_Tir.ics', 'w') as my_file:
        my_file.writelines(c.serialize_iter())
        
def sanitize_word(word):
    #Remove '{{' and '}}' from the given word.
    return re.sub(r'{{(.*?)}}', r'\1', word)

#Assurer vous d'avoir remplir au préalable le fichier information.csv en utilisant excel ou manuellement. Si vous avez du soucis, demande à un information à proximitée    
def gen_mdfile():
    
    df = pd.read_csv('valConst.csv',sep=";",index_col=0)
        
    
    annee = current_year = datetime.now().year
    nbMembre = len(df.loc["PRESENT_MEMBERS"][0].split(','))
    lstExtentless = []
    
    
    lstACalc = {"YEAR" : str(annee), "NB_PRESENT" : str(nbMembre), "ANNEE_PRECEDENT" : str(annee-1)}
    lstFile = os.listdir("template")
    for file in lstFile:
        lstExtentless.append(file[:-3])
    
    for filename in lstExtentless:
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
        t = open(f'./{filename}_{annee}.md', 'w') 
        t.write(md_content)
        t.close()

#init_document()
#export_to_calendar()
gen_mdfile()


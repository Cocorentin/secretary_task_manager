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


CUR_YEAR_PATH = sys.path[0] + "/" + str(datetime.now().year)


def init_document():
    pathlib.Path(CUR_YEAR_PATH).mkdir(exist_ok=True)
    
    
def get_pdf_data(cur_page,lst_val):
    pattern_row_data = re.compile("^(\d{2}.\d{2}.\d{4}).*")

    for entry in cur_page:
        if pattern_row_data.match(entry):
            lst_val.append(entry.split(" "))
        
    
    
#Renvoi un ics avec des dates formater à UTC+2
def export_to_calendar() -> []:

    # creating a pdf reader object
    reader = PdfReader('2025_Data/Annonce des jours de tirs_2025_03022025.pdf')

    entry_data = []
    fairpart_data = []
    
    #for each page, we extract the text and split into array before matching it
    for x in range(len(reader.pages)):
        page = reader.pages[x]
        raw_text = page.extract_text()
        split_txt = raw_text.splitlines()
        get_pdf_data(split_txt,entry_data)
    
    
    #Create ISC
    delim = "-"
    c = Calendar()
    for entry in entry_data:
        e = Event()
        ymd = entry[0].split(".")
        ymd[0], ymd[2] = ymd[2], ymd[0]
        fairpart_data.append([ymd[0] + "." + ymd[1] + "." + ymd[2],entry[1],entry[2],entry[4]])
        date_event = delim.join(ymd)
        e.name = "Évenement de type " + entry[4]
        e.begin = datetime.fromisoformat(date_event +"T" + entry[1] +":00+02:00")
        e.end = datetime.fromisoformat(date_event +"T" + entry[2] + ":00+02:00")
        e.classification()
        c.events.add(e)
    c.events
    # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
    with open( CUR_YEAR_PATH +'/Date_Tir.ics', 'w') as my_file:
        my_file.writelines(c.serialize_iter())
    return fairpart_data
        
def sanitize_word(word):
    #Remove '{{' and '}}' from the given word.
    return re.sub(r'{{(.*?)}}', r'\1', word)
        

x = md_generator()

lst_file = x.get_template_name()
lst_size = len(lst_file)

#init_document()
#lst_date = export_to_calendar()
#gen_mdfile()


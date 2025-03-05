import os
import sys
from datetime import datetime
import pathlib
#from pdfquery import PDFQuery0
from ics import Calendar, Event, Todo
from datetime import datetime
import time
#Extract Data into array here
from pypdf import PdfReader
import re
import pandas as pd
from markdown_pdf import MarkdownPdf,Section
from script.user_interface import user_interface




def init_document():
    pathlib.Path(CUR_YEAR_PATH).mkdir(exist_ok=True)
    
    

        

        

x = user_interface()
x.run()


#init_document()
#lst_date = export_to_calendar()
#gen_mdfile()


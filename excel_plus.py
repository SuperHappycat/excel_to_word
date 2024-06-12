import pandas as pd
import pyperclip
import docx
import time
bugfixtime = 0
def excel_to_word(excel, wordname):
    time.sleep(bugfixtime)
    df = pd.read_excel(excel + ".xlsx", sheet_name="Sheet1")
    time.sleep(bugfixtime)
    excel_string = df.to_string()
    time.sleep(bugfixtime)
    pyperclip.copy(excel_string)
    time.sleep(bugfixtime)
    doc = docx.Document()
    time.sleep(bugfixtime)
    doc.add_paragraph(pyperclip.paste())
    time.sleep(bugfixtime)
    doc.save( wordname + ".docx")
    time.sleep(bugfixtime)
def bugfix(timep):
    bugfixtime = timep
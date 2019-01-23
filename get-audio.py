#!PATH TO PYTHON INTERPRETER e.g: /usr/local/bin/python3.6

import cgi
from polly_process import Polly
from urllib.parse import unquote
import traceback
from bs4 import BeautifulSoup #needed if there are html tags in the text

print("Content-Type: application/json\r\n")

try:
    form = cgi.FieldStorage()
    txt = unquote(form.getvalue('txt'))
    langauge = form.getvalue('language')
    gender = form.getvalue('gender')

    ####use below two lines if there is html tags in the text
    soup = BeautifulSoup(txt)
    txt = soup.get_text() #remove html tags
    ################

    pollyObj = Polly(txt, langauge, gender)
    responsePolly = pollyObj.sendPollyRequest()
    print(responsePolly)

except Exception as e:
    f = open('log.txt', 'w')
    f.write(str(e))
    f.write(traceback.format_exc())
    f.close()
    
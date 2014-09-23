import requests
from pattern import web
import time
import tkMessageBox

url = 'http://travel.state.gov/content/visas/english/law-and-policy/bulletin/2014/visa-bulletin-for-september-2014.html'

while True:
    time.sleep(60)

    r = requests.get(url)

    if not u'404 - Page Not Found' in r.text:
        tkMessageBox.showwarning("Bulletin released","Bulletin released")
        break

    


     
import requests
from pattern import web
import fnmatch

def find_governor_races(str):
    races = []
    pattern = 'http://www.realclearpolitics.com/epolls/20??/governor/??/*.html'
    dom = web.Element(str)

    for elem in dom.by_tag('a'):
        if u'href' in elem.attributes:
            link = elem.attributes['href']
            if fnmatch.fnmatch(link, pattern):
                races.append(link)

    return races


url = u'http://www.realclearpolitics.com/epolls/2010/governor/2010_elections_governor_map.html'
r = requests.get(url)
print find_governor_races(r.text), '\n'


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
from pattern import web
import xml.etree.ElementTree as ET

def recurse_node(indent, element):
    tabspace = indent * ' '
    print tabspace + element.tag

    lastTag =''
    for child in element:
        if child.tag == lastTag:
            break
        recurse_node(indent + 1, child)
        lastTag = child.tag

def get_poll_xml(id):
    url = u'http://charts.realclearpolitics.com/charts/{0}.xml'.format(id)
    r = requests.get(url)
    return r.text

#xmlText  = get_poll_xml(1044)

xmlText = '''
    <chart>
    <series>
    <value xid="0">1/27/2009</value>
    <value xid="1">1/28/2009</value>
    </series>
    <graphs>
    <graph gid="1" color="#000000" balloon_color="#000000" title="Approve">
    <value xid="0">63.3</value>
    <value xid="1">63.3</value>
    </graph>
    <graph gid="2" color="#FF0000" balloon_color="#FF0000" title="Disapprove">
    <value xid="0">20.0</value>
    <value xid="1">20.0</value>
    </graph>
    </graphs>
    </chart>
    '''

dom = web.Element(xmlText)



listDates = []
series = dom.by_tag('series')
values = series[0].by_tag('value')
for value in values:
    listDates.append(value.content)

frame = pd.DataFrame({'date': pd.to_datetime(listDates)})

print frame
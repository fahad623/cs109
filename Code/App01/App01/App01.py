

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
    proxyDict = { 
              "http"  : "web-proxy.houston.hp.com:8088", 
              "https" : "web-proxy.houston.hp.com:8088" 
              }

    url = u'http://charts.realclearpolitics.com/charts/{0}.xml'.format(id)
    r = requests.get(url, proxies=proxyDict)
    return r.text



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
#xmlText  = get_poll_xml(1044)
dom = web.Element(xmlText)


dates = dom.by_tag('series')[0]
frame = pd.DataFrame({'date': pd.to_datetime([str(n.content) for n in dates.by_tag('value')])})

for graph in dom.by_tag('graph'):
    name = graph.attributes['title']

    frame[name] = [float(n.content) if n.content else np.nan for n in graph.by_tag('value')]

#for graph in dom.by_tag('graph'):
#    title = (graph.attributes['title'])
#    values = graph.by_tag('value')
#    listGraphValues = []
#    for value in values:
#        listGraphValues.append(value.content)

#    s = np.array(listGraphValues)
#    s[s==''] = '0'
#    s.astype(float)
#    frame[title] = s

frame = frame.sort(columns = ['date'])
print frame
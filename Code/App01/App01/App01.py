

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

#root = ET.fromstring(get_poll_xml(1044))
#recurse_node(0, root)
dom = web.Element(get_poll_xml(1044))
result = {}
for graph in dom.by_tag('graph'):
    title = _strip(graph.attributes['title'])
    result[title] = graph.attributes['color']
print result
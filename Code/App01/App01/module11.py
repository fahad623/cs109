import networkx as nx
import json

vote_data = json.load(open(r'C:\Fahad\code\Python-projects\cs109\content-original\vote_data.json'))

senators = set(x['display_name'] for d in vote_data for vote_grp in d['votes'].values() for x in vote_grp)
weights = {s: {ss: 0 for ss in senators if ss != s} for s in senators}

a = 9
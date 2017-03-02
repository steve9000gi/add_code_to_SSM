#!/usr/bin/env python

""" add_code_to_SSM.py: Add the code from the associated Coded Binary Link
        Matrix (CBLM) to a System Support Map (SSM).

"""

import sys
import logging
import json
import csv
from numpy import genfromtxt
from pprint import pprint

logger = logging.getLogger(__name__)
logging.basicConfig(level=3, format="%(asctime)-15s %(message)s")

ssm = sys.argv[1]
cblm = sys.argv[2]

logger.error('ssm: ' + ssm + '; cblm: ' + cblm)

with open(ssm) as jf: # Read in ssm.json file
    j = json.load(jf)

nodes = j["nodes"]
print "type(nodes):" + type(nodes).__name__
print "# nodes:" , len(nodes)
#for i, node in enumerate(nodes):
#    name = node["name"]
#    nodes[i]["code"] = "code #" + str(i)
#    print  "node[" + str(i) + "][\"name\"]: " + nodes[i]["name"]
#    print  "node #" + str(i) + "[\"name\"]: " + name + "; type: " + type(node).__name__

#pprint(nodes)
clist = []

with open(cblm) as cf: # Read in CBLM file as list of strings, each string a row:
    rows = cf.read().split("\n");

for row in rows: # clist becomes a list of sublists, each sublist a row
    r = row.split("\t") # Split each row into a list of items
#    print(len(r))
    clist.append(r)

clist.pop() # get rid of empty last row

node_id_index = 1 # position for NodeID column in CBLM
code_index = 4    # position for Code column in CBLM

for i, c_node_line in enumerate(clist[1:]): # skipping headers, select each line from CBLM
    print "row " + str(i) + ": nodeID: " + c_node_line[node_id_index] + "; Code: " + c_node_line[code_index]
    # Now find which node in nodes has the same NodeID as the current c_node_line.
    #  node = (item for item in nodes if item["id"] == c_node_line[node_id_index]).next()

    # Then, add {'code': c_node_line[code_index]} to that node.
#    node["code"] = c_node_line[code_index]
    for j_ix, j_node in enumerate(nodes): # Step through each node from ssm.json file
#	print type(j_node["id"]).__name__ + " ?== " + type(c_node_line[node_id_index]).__name__
	print str(j_ix) + ": name: " + j_node["name"] + "; id: " + str(j_node["id"]) + " ?== " + c_node_line[code_index]
	if str(j_node["id"]) == c_node_line[node_id_index]: # If the ids match...
	    print "node w/ id " + str(j_node["id"]) + " gets code = '" + c_node_line[code_index] + "'"
	    j_node["code"] = c_node_line[code_index]   # ...then put the code from the CBLM into the json.

pprint(j)

# Finally, write the coded json to file:

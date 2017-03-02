#!/usr/bin/env python

""" add_code_to_SSM.py: Add the code from the associated Coded Binary Link
        Matrix (CBLM) to a System Support Map (SSM).

"""

import sys
import os
import json

ssm = sys.argv[1]
cblm = sys.argv[2]

print 'ssm: ' + ssm + '; cblm: ' + cblm

with open(ssm) as json_input_file: # Read in ssm.json file
    json_object = json.load(json_input_file)

nodes = json_object["nodes"]
print "type(nodes):" + type(nodes).__name__
print "# nodes:" , len(nodes)

clist = []

with open(cblm) as cblm_file: # Read CBLM file as list, each item a row:
    rows = cblm_file.read().split("\n");

for row in rows: # clist becomes a list of sublists, each sublist a row
    r = row.split("\t") # Split each row into a list of items
    clist.append(r)

clist.pop() # get rid of empty last row

node_id_index = 1 # position for NodeID column in CBLM
code_index = 4    # position for Code column in CBLM

for c_node_line in clist[1:]: # Skipping headers, select each row
    # Find which node in json object nodes has the same id  as the NodeID in
    # the current c_node_line:
    for j_ix, j_node in enumerate(nodes): # Look at each node from json object
	if str(j_node["id"]) == c_node_line[node_id_index]:
	    j_node["code"] = c_node_line[code_index] # Add matching code
	    break

# Finally, write the json object with codes added to file:
outfilename = os.path.splitext(ssm)[0] + "-C.json"
print outfilename
with open(outfilename, "w") as outfile:
    json.dump(json_object, outfile)

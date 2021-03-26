# this file will convert the easier to write json format to XML.

import plistlib , json, sys


src= sys.argv[1]  

if src.endswith('json'):
    json_text = json.load(open(src))
    plistlib.writePlist(json_text , sys.argv[2])

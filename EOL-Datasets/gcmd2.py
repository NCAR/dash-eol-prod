from lxml import objectify
import pandas as pd
import os
from xml.etree import ElementTree

filename = "2.002.xml"
namespaces = {'gmd': 'http://www.isotc211.org/2005/gmd' , 'gco': 'http://schemas.isotc211.org/19115/-3/gco/1.0'}

dom = ElementTree.parse(filename)
party = dom.findall('gmd:identificationInfo',namespaces)
for part in party:
    print(part.text)
#print(party)

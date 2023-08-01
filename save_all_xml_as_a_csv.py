import csv
import os
import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom
from os import listdir
import sys



path = "C:/Users/matjul/Documents/Datenkompass/fair_enough/Parsen in Python/sample_xml" #folder containing all xml files. py-file needs to be saved in the same folder
dir = os.listdir(path)

for file in dir:
    print (file) # prints a name of a xml-file

    tree = ET.parse(file)
    root = tree.getroot()

#for x in root[0][0]:
#    print(x.tag, x.attrib) #identifiers

#for x in root[0][0]:
#    print(x.text)  #identifiers values

    for x in root.findall('.//IDENTIFIERS'):
        pid =x.find('PRIMARY_ID').text
      #  print(pid)

    ltag = []        #create a list with all values marked as "TAG"
    lvalue = []      #create a list with all values marked as "VALUE"

    for x in root.findall('.//SAMPLE_ATTRIBUTE'):  # parse all that is in SAMPLE_ATTRIBUTES
        tag =x.find('TAG').text
        value =x.find('VALUE').text
        ltag.append(tag)
        lvalue.append(value)
      #  print(tag)
      #  print(value)

    filename = "%s.csv" %pid  #each csv is named according to Primary ID 
    filepath = "C:/Users/matjul/Documents/Datenkompass/fair_enough/Parsen in Python/sample1_xml/sample_c"   #folder where csv-files should be saved
    
    path = os.path.join(filepath, filename)

    csvfile = open(path,'w',encoding='utf-8')
    #csvfile_writer = csv.writer(csvfile, lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL) # define writer; separate with tab; lineterminator so there is no empty row beetween | delimiter='\t' to separate as a tab |  quotechar='"', quoting=csv.QUOTE_ALL to put each value in double quote
    csvfile_writer = csv.writer(csvfile, delimiter='\t', lineterminator='\n')

    csvfile_writer.writerow(["PRIMARY ID", "TAG", *ltag])
    csvfile_writer.writerow([pid, "VALUE", *lvalue])

csvfile.close()


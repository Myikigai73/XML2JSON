
# -*- coding: utf-8 -*-

# Program to convert an xml
# file to json file
 
# import json module and xmltodict
# module provided by python
import json
import xmltodict
 
 
# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
with open("test.xml") as xml_file:
     
    data_dict = xmltodict.parse(xml_file.read())
    # xml_file.close()
     
    # generate the object using json.dumps()
    # corresponding to json data
     
    json_data = json.dumps(data_dict)
     
    # Write the json data to output
    # json file
    with open("data.json", "w") as json_file:
        json_file.write(json_data)
        # json_file.close()
        
        
import json
from pymongo import MongoClient
 
 
# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")
  
# database
db = myclient["GFG"]
  
# Created or Switched to collection
# names: GeeksForGeeks
Collection = db["data"]
 
# Loading or Opening the json file
with open('data.json') as file:
    file_data = json.load(file)
     
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
if isinstance(file_data, list):
    Collection.insert_many(file_data) 
else:
    Collection.insert_one(file_data)

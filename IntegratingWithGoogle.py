import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import yaml
import pprint


with open('config.yml','r') as file:
    doc = yaml.full_load(file)



credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', doc['scopes'])
client = gspread.authorize(credentials)

spreadsheet = client.open('func')

with open('funcs.csv', 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests, zipfile, io
import json
import datetime
import pathlib
import lxml
import xlrd
import xmltodict


class EV_Charger:
    """ 
    Class to download files from REE 
    """
    def __init__(self):
        
        pd.set_option("display.max_rows", None, "display.max_columns", None)


    def api_call_method (self):
        '''performs the API call'''
        
        url = 'https://infocar.dgt.es/datex2/v3/miterd/EnergyInfrastructureTablePublication/electrolineras.xml'
    
        r = requests.request(
            "GET",
            url,
        )

        print('Request Status '+str(r.status_code))
        print(r.headers['content-type'])
        print(r.text)
        data = r.text

        data_parsed = xmltodict.parse(data)

        return data_parsed





test = EV_Charger()
x = test.api_call_method()  

print('-------------------------Space-------------------------')

dict_data = x['d2:payload']['egi:energyInfrastructureTable']['egi:energyInfrastructureSite']

for i in dict_data:
    print(i)


# for x, y in dict_data.items():
#     print(x, y)


keysdic = list(x)




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


class ev_chargers:
    """ 
    Class to download files from REE 
    """
    def __init__(self):
        
        pd.set_option("display.max_rows", None, "display.max_columns", None)


    def api_call_method (self):
        '''performs the API call'''

        global data_parsed

        global data_parsed_v1
        global data_parsed_v2

        
        url = 'https://infocar.dgt.es/datex2/v3/miterd/EnergyInfrastructureTablePublication/electrolineras.xml'
    
        r = requests.request(
            "GET",
            url,
        )

        print('Request Status '+str(r.status_code))
        print(r.headers['content-type'])
        # print(r.text)
        data = r.text

        data_parsed = xmltodict.parse(data)

        print(data)

        data_parsed_v2 = pd.json_normalize(data_parsed,record_path=['d2:payload','egi:energyInfrastructureTable','egi:energyInfrastructureSite'])

        return data_parsed

    def ev_dataframe (self):
            return self.data_processing()
        


ev_class = ev_chargers()


dataframe = ev_class.api_call_method()  

# dataframe = ev_class.data_processing()  


# dataframe = ev_class.ev_dataframe()  








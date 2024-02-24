

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
        # print(r.text)
        data = r.text

        data_parsed = xmltodict.parse(data)

        data_parsed = data_parsed['d2:payload']['egi:energyInfrastructureTable']['egi:energyInfrastructureSite']


        return data_parsed


    def data_processing (self):

        dict_data = self.api_call_method()

        empty_list = []

        for i in dict_data:
            # print(i.items())
            flat = pd.json_normalize(i)
            print(flat)
            empty_list.append(flat)

        final = pd.concat(empty_list,axis=0,join='outer')

        return final
        

    def ev_dataframe (self):
            return self.data_processing()
        




ev_class = EV_Charger()

dataframe = ev_class.ev_dataframe()  








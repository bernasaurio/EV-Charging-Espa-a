
from ev_class import ev_chargers
import matplotlib.pyplot as plt

import plotly.express as px
import pandas as pd



if __name__ == '__main__':


    ev_class = ev_chargers()
    dataframe = ev_class.ev_dataframe()  

    print(dataframe.keys())




    # plotting map using plotl
    fig = px.scatter_geo(dataframe, lat = 'fac:locationReference.loc:coordinatesForDisplay.loc:latitude', lon = 'fac:locationReference.loc:coordinatesForDisplay.loc:longitude', color='fac:operator.fac:name.com:values.com:value.#text')

    # setting title for the map
    fig.update_layout(title = 'test', title_x = 0.5)

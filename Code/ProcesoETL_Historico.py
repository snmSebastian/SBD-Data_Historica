#Liberia
import pandas as pd

#Permite buscar y recuperar una lista de nombres de archivos que coinciden con un patrón específico de nombre
#de archivo en un directorio o en una jerarquía de directorios.
import glob

import numpy as np
import os
from datetime import datetime, timedelta

# Data  Historica

# utilizamos la función glob para crear una lista de rutas de archivo que coinciden con el patrón *Chile Mensual*.csv
# en el directorio path_chi_men. Esto nos da una lista de todas las rutas de archivo que cumplen con el patrón en el
# directorio.

path_data_historica_fill_rate= r'C:\Users\SSN0609\OneDrive - Stanley Black & Decker\Dashboards LAG\Data Flow\Master Products_Customers\Data_Historica\Fill Rate'
path_data_historica_sales= r'C:\Users\SSN0609\OneDrive - Stanley Black & Decker\Dashboards LAG\Data Flow\Master Products_Customers\Data_Historica\Sales'
path_data_historica_demand= r'C:\Users\SSN0609\OneDrive - Stanley Black & Decker\Dashboards LAG\Data Flow\Master Products_Customers\Data_Historica\Demand'

all_files_fill_rate= glob.glob(path_data_historica_fill_rate+"/*Fill Rate*.xlsx")
all_files_sales= glob.glob(path_data_historica_sales+"/*Sales*.xlsx")
all_files_demand= glob.glob(path_data_historica_demand+"/*Demand*.xlsx")


lst_Fill_Rate=[]
lst_Demand=[]
lst_Sales=[]

for filename in all_files_fill_rate:
    df=pd.read_excel(filename,index_col=None,header=0,dtype=str)
    lst_Fill_Rate.append(df)

for filename in all_files_sales:
    df=pd.read_excel(filename,index_col=None,header=0,dtype=str)
    lst_Sales.append(df)

for filename in all_files_demand:
    df=pd.read_excel(filename,index_col=None,header=0,dtype=str)
    lst_Demand.append(df)

df_fill_rate=pd.concat(lst_Fill_Rate,axis=0,ignore_index=True)
df_sales=pd.concat(lst_Sales,axis=0,ignore_index=True)
df_demand=pd.concat(lst_Demand,axis=0,ignore_index=True)

ruta_fill_rate = r'C:\Users\SSN0609\OneDrive - Stanley Black & Decker\Dashboards LAG\Data Flow\Master Products_Customers\Data_Historica\Dataflow\fill_rate_historico.csv'
ruta_sales = r'C:\Users\SSN0609\OneDrive - Stanley Black & Decker\Dashboards LAG\Data Flow\Master Products_Customers\Data_Historica\Dataflow\Sales_historico.csv'
ruta_demand = r'C:\Users\SSN0609\OneDrive - Stanley Black & Decker\Dashboards LAG\Data Flow\Master Products_Customers\Data_Historica\Dataflow\Demand.historico.csv'


df_fill_rate.to_csv(ruta_fill_rate, index=False)
df_sales.to_csv(ruta_sales, index=False)
df_demand.to_csv(ruta_demand, index=False)
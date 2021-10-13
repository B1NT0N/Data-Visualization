import numpy as np
import pandas as pd
from openpyxl import load_workbook
import time 
import sqlalchemy
from datetime import date

# engine = sqlalchemy.create_engine("mysql://root@localhost/smscount")
# sql = pd.read_sql('sms', engine)
# print(sql)
start = time.time()

# try:
#     try:
#         df = pd.read_csv("LuxDev - Saida2021.csv")
#     except (UnicodeDecodeError, NameError): 
#         print("Changing Encoding")
#         df = pd.read_csv("LuxDev - Saida2021.csv",encoding='ISO-8859-1')
        
#     df=df.drop(df.columns[[3,5,6,7,8,9,10,11,13,14]],axis=1)
     
#     # df=df.drop(columns=
#     #         [   "SMSC",
#     #             #"Estado",
#     #             "Comutador",
#     #             #"Conta Destino",
#     #             "Processo",
#     #             "Célula Origem",
#     #             "Célula Destino",
#     #             "IMSI Origem",
#     #             "IMSI Destino",
#     #             "Conta Origem",
#     #             "MtMscAddress",
#     #             "Tipo SMS"
#     #             ], axis=1
#     #         )
    
#     df = df.set_index(list(set(df.columns[[3]])))
    
#     df = df.drop([2], axis=0)
#     df = df.drop([3], axis=0)
#     df.reset_index(inplace = True)
#     df = df.drop(df.columns[[0]],axis=1)
 
    
#     if True == True: #Entrada
#         df=df.replace(to_replace="Gateway_G", value=1,)
#         df.rename({df.columns.values[3]:'Tipo'},axis=1,inplace=True)
#         print(df.tail(5))
#     else:
#         df=df.replace(to_replace="Gateway_G", value=2,)
#         df=df.replace(to_replace="p2pcpvmovel", value=3,)
#         df=df.replace(to_replace="ToIbasisA2P", value=2,)
#         df=df.rename({df.columns.values[3]: 'Tipo'})
#         print(df.tail(5))
    
# except Exception as exception:
#     print(exception)
 
print("Current month:", '{:02d}'.format(date.today().month))
            
end = time.time()
print("Total runtime:", (end-start))

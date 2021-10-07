import streamlit as st
import numpy as np
import pandas as pd
import sqlalchemy

def load_data(file):
    
    engine = sqlalchemy.create_engine('mysql://root@localhost/smscount')
    
    df = pd.read_csv(file,encoding='utf-8')
    df=df.drop(df.columns[[3,5,6,7,8,9,10,11,13,14]],axis=1)
    
    df = df.set_index(list(set(df.columns[[3]])))
    df = df.drop([2], axis=0)
    df = df.drop([3], axis=0)
    df.reset_index(inplace = True)
    df = df.drop(df.columns[[0]],axis=1)
    
    if selection == "Entrada": 
        df=df.replace(to_replace="Gateway_G", value=1,)
        df=df.replace(to_replace="-", value=1,)
        df.rename({df.columns.values[3]:'Tipo'},axis=1,inplace=True)
        st.write(df.head(25))
        print(df.head(5))
    else:
        df=df.replace(to_replace="Gateway_G", value=2,)
        df=df.replace(to_replace="p2pcpvmovel", value=3,)
        df=df.replace(to_replace="ToIbasisA2P", value=3,)
        df.rename({df.columns.values[3]:'Tipo'},axis=1,inplace=True)
        st.write(df.head(25))
        print(df.head(5))
    st.success("Done")
    
    df.to_sql('sms', engine, if_exists='replace', index=False)

st.title('Data Visualization')

file = st.file_uploader("", type=".csv", accept_multiple_files=False, key=None, help="Upload Data",)

selection = st.radio("", ["Entrada","Saida"])

add_button = st.button("Add Data", help="Click to confirm the Upload")

if add_button==True and file is not None:
    load_data(file)
elif add_button==True and file is  None:
    st.warning("Please Upload a File")

import streamlit as st
import numpy as np
import pandas as pd
import sqlalchemy


engine = sqlalchemy.create_engine('mysql://root@localhost/smscount')

def show_data(year,month):
    df1 = pd.read_sql("SELECT Origem, COUNT(CASE WHEN Tipo = 1 then 1 ELSE NULL END) as OnNet, COUNT(CASE WHEN Tipo = 2 then 1 ELSE NULL END) as OffNet, COUNT(CASE WHEN Tipo = 3 then 1 ELSE NULL END) as Internacional, DATE_FORMAT(Data, '%%m-%%y') as Mes FROM sms Group By Origem", engine)
    st.write(df1)

def load_data(file):
    st.markdown("---")
    df = pd.read_csv(file,encoding='utf-8')
    df=df.drop(df.columns[[3,5,6,7,8,9,10,11,13,14]],axis=1)
    
    df = df.set_index(list(set(df.columns[[3]])))
    df = df.drop([2], axis=0)
    df = df.drop([3], axis=0)
    df.reset_index(inplace = True)
    df = df.drop(df.columns[[0]],axis=1)
    df.rename({df.columns.values[2]:'Data'},axis=1,inplace=True)
    
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

st.set_page_config(page_title='SMSBulk A2P', page_icon="Logo-s.png",layout="centered")
st.write('')
st.write('')
st.image("CVMOVEL HORIZONTAL OFICIAL - POSITIVA.png", width=100)

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

with st.container():
    _0,_1,_2 = st.columns([0.6,1,0.25])
    with _1:
        st.markdown('<h1 style= color:#1cb4c4;">SMSBulk A2P</h1>', unsafe_allow_html=True)

    file = st.file_uploader("", type=".csv", accept_multiple_files=False, key=None, help="Upload Data",)

    col1, col2 = st.columns([3,0.60])

    with col1:
        selection = st.radio("", ["Entrada","Saida"])
    with col2:
        st.write('')
        st.write('')
        add_button = st.button("Adicionar", help="Click to confirm the Upload")
st.markdown("---")
with st.container():
    st.write('')
    col3,col4,col5 = st.columns([1,1,0.32])
    with col3:

        year = st.selectbox('Ano', range(1990, 2100))
    with col4:
        month = st.selectbox('Mês', range(1, 13))
    with col5:
        st.write('')
        st.write('')

        filter_button = st.button("Filtrar", help="Click to confirm the Upload")


        
if add_button==True and file is not None:
    load_data(file)
elif add_button==True and file is  None:
    st.warning("Please Upload a File")
elif filter_button == True:
    show_data(year,month)
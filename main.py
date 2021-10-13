import streamlit as st
import numpy as np
import pandas as pd
import sqlalchemy
from datetime import date

Username= "epiz_30055294"
Database_name= "epiz_30055294_smscount"
Password= "cBdfVbBLA7l"
Server= "sql108.epizy.com"
Port= "3306"

engine = sqlalchemy.create_engine(f'mysql://{Username}:{Password}@{Server}:{Port}/{Database_name}')

def show_data(year,month):
    my_bar = st.progress(0)
    df1 = pd.read_sql(f"SELECT Origem, COUNT(CASE WHEN Tipo = 1 then 1 ELSE NULL END) as OnNet, COUNT(CASE WHEN Tipo = 2 then 1 ELSE NULL END) as OffNet, COUNT(CASE WHEN Tipo = 3 then 1 ELSE NULL END) as Internacional, DATE_FORMAT(Data, '%%m-%%y') as Mes FROM sms where Data between '{year}-{month}-01' and '{year}-{month}-31' Group By Origem", engine)
    
    my_bar.progress(50)
    if df1.empty:
        my_bar.progress(100)
        st.warning("Nenhum Resultado Encontrado")
    else:
        
        _a,_b,_c = st.columns([0.1,3,0.2])
        with _b:
            st.success("Concluido")
            st.dataframe(df1)
            @st.cache
            def convert_df(df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                return df.to_csv().encode('utf-8')

            csv = convert_df(df1)

            st.download_button(
                label="Download Data",
                data=csv,
                file_name=f'Output {month}/{year}.csv',
                mime='text/csv',
            )
        my_bar.progress(100)
        
def load_data(file):
    st.markdown("---")
    my_bar = st.progress(0)
    df = pd.read_csv(file,encoding='utf-8')
    
    my_bar.progress(25)
    df=df.drop(df.columns[[3,5,6,7,8,9,10,11,13,14]],axis=1)
    df = df.set_index(list(set(df.columns[[3]])))
    df = df.drop([2], axis=0)
    df = df.drop([3], axis=0)
    df.reset_index(inplace = True)
    df = df.drop(df.columns[[0]],axis=1)
    df.rename({df.columns.values[2]:'Data'},axis=1,inplace=True)
    
    my_bar.progress(50)
    if selection == "Entrada": 
        df=df.replace(to_replace="Gateway_G", value=1,)
        df=df.replace(to_replace="-", value=1,)
        df.rename({df.columns.values[3]:'Tipo'},axis=1,inplace=True)
        # st.write(df.head(25))
        print(df.head(5))
    else:
        df=df.replace(to_replace="Gateway_G", value=2,)
        df=df.replace(to_replace="p2pcpvmovel", value=3,)
        df=df.replace(to_replace="ToIbasisA2P", value=3,)
        df.rename({df.columns.values[3]:'Tipo'},axis=1,inplace=True)
        # st.write(df.head(25))
        print(df.head(5))
    
    
    my_bar.progress(75)
    df.to_sql('sms', engine, if_exists='append', index=False)
    my_bar.progress(100)
    st.success("Concluido")

st.set_page_config(page_title='SMSBulk A2P', page_icon="https://raw.githubusercontent.com/B1NT0N/Data-Visualization/master/logo-s.png?token=ARBWDNLDKHLCQOUCXVUSTS3BN25AS",layout="centered")
st.write('')
st.write('')
st.image("https://raw.githubusercontent.com/B1NT0N/Data-Visualization/master/CVMOVEL%20HORIZONTAL%20OFICIAL%20-%20POSITIVA.png?token=ARBWDNN2Y2OP5EB2DEFLWV3BN24YK", width=100)

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
.css-fk4es0 {
    background-image:linear-gradient(90deg, rgb(228,49,23), rgb(37,184,202));
}
</style> """, unsafe_allow_html=True)

with st.container():
    _0,_1,_2 = st.columns([0.6,1,0.25])
    with _1:
        st.markdown('<h1 style= color:#1cb4c4;">SMSBulk A2P</h1>', unsafe_allow_html=True)

    file = st.file_uploader("", type=".csv", accept_multiple_files=False, key=None,)

    col1, col2 = st.columns([3,0.60])

    with col1:
        selection = st.radio("", ["Entrada","Saida"])
    with col2:
        st.write('')
        st.write('')
        add_button = st.button("Adicionar", help="")
st.markdown("---")
with st.container():
    st.write('')
    col3,col4,col5 = st.columns([1,1,0.32])
    with col3:
        
        year = st.selectbox('Ano', range((date.today().year-3), date.today().year))
    with col4:
        month = st.selectbox('Mês', ["01","02","03","04","05","06","07","08","09","10","11","12"])
    with col5:
        st.write('')
        st.write('')

        filter_button = st.button("Filtrar", help="")
      
if add_button==True and file is not None:
    load_data(file)
elif add_button==True and file is  None:
    st.warning("Please Upload a File")
elif filter_button == True:
    show_data(year,month)
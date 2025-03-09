# Data manipulation
import numpy as np
import datetime as dt
import pandas as pd
import geopandas as gpd

# Database and file handling
import os

# Data visualization
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import graphviz
import pydeck as pdk

path_cda = '\\CuriosityDataAnalytics'
path_wd = path_cda + '\\wd'
path_data = path_wd + '\\data'

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
    img[data-testid="stLogo"] {
                height: 6rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("What's new in Streamlit 1.41?")
st.divider()

with st.sidebar:
    st.logo(path_cda + '\\logo.png', size='large')
    st.empty()
#
#

def page1():
    st.header(':one: st.metric and st.columns border')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.40')
    cols[1].subheader('Streamlit 1.41')

    cols[0].code('''
        st.metric(label='Average Price', value='$40.28', delta='$1.47')
    ''')
    cols[0].metric(label='Average Price', value='$40.28', delta='$1.47')

    cols[1].code('''
        st.metric(label='Average Price', value='$40.28', delta='$1.47', border=True)
    ''')
    subcols = cols[1].columns(4)
    subcols[0].metric(label='Average Price', value='$40.28', delta='$1.47', border=True)



    cols[0].code('''
        cols = st.columns(4)
        for i, j in enumerate(cols):
            cols[i].image('image.png')
    ''')
    subcols = cols[0].columns(4)
    for i, j in enumerate(subcols):
        subcols[i].image(path_cda + '\\logo.png')

    cols[1].code('''
        cols = st.columns(4, border=True)
        for i, j in enumerate(cols):
            cols[i].image('image.png')
    ''')
    subcols = cols[1].columns(4, border=True)
    for i, j in enumerate(subcols):
        subcols[i].image(path_cda + '\\logo.png')




def page2():
    st.header(':two: Pinned columns')

    np.random.seed(42)
    data = {
        "Type": [f"Type {i}" for i in range(1, 11)],
    }
    for year in range(1980, 2024):
        data[str(year)] = np.random.rand(10) * 100
    df = pd.DataFrame(data)
    
    st.subheader('Streamlit 1.40')
    st.code('''
        st.data_editor(df, hide_index=True)    
    ''')
    st.data_editor(df, hide_index=True)  

    st.subheader('Streamlit 1.41')
    st.code('''
        st.data_editor(
            df,
            column_config={"Type": st.column_config.Column(pinned=True)},
            hide_index=True
        )
    ''') 
    st.data_editor(
        df,
        column_config={"Type": st.column_config.Column(pinned=True)},
        hide_index=True
    )




def page3():
    st.header(':three: st.button tertiary type')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.40')
    cols[1].subheader('Streamlit 1.41')

    cols[0].code('''
        st.button('primary', type='primary')
        st.button('secondary', type='secondary')    
    ''')
    subcols = cols[0].columns(6)
    subcols[0].button('primary', type='primary', key='t1')
    subcols[1].button('secondary', type='secondary', key='t2')

    cols[1].code('''
        st.button('primary', type='primary')
        st.button('secondary', type='secondary')    
        st.button('tertiary', type='tertiary')  
    ''')
    subcols = cols[1].columns(6)
    subcols[0].button('primary', type='primary', key='t3')
    subcols[1].button('secondary', type='secondary', key='t4')
    subcols[2].button('tertiary', type='tertiary', key='t5')



def page4():
    st.header(':four: st.date_input ISO formatted string')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.40')
    cols[1].subheader('Streamlit 1.41')

    cols[0].code('''
        import datetime as dt
        st.date_input('Date', value=dt.date(2024,1,1), format='YYYY-MM-DD')
    ''')
    cols[0].date_input('Date', value=dt.date(2024,1,1), format='YYYY-MM-DD')

    cols[1].code('''
        st.date_input('Date', value='2024-01-01', format='YYYY-MM-DD')
        .
    ''')
    cols[1].date_input('Date', value='2024-01-01', format='YYYY-MM-DD', key='dt')

pg = st.navigation([st.Page(page1, title='st.metric and st.columns border'),
                    st.Page(page2, title='Pinned columns'),
                    st.Page(page3, title='st.button tertiary type'),
                    st.Page(page4, title='st.date_input ISO formatted string')])
pg.run()